#include <stdio.h>
#include <stdlib.h>
#include <OS.h>

#define BUFFER_SIZE 5
#define MAX_ITEMS 20

int buffer[BUFFER_SIZE];
int in = 0;
int out = 0;
int produced_count = 0;
int consumed_count = 0;

sem_id mutex;
sem_id full;
sem_id empty;

int32 producer(void* arg) {
   int item = 1;

   while (produced_count < MAX_ITEMS) {
      acquire_sem(empty);
      acquire_sem(mutex);

      buffer[in] = item;
      printf("Produced: %d\n", item);
      item++;
      in = (in + 1) % BUFFER_SIZE;

      produced_count++;

      release_sem(mutex);
      release_sem(full);
   }

   return 0;
}

int32 consumer(void* arg) {
   while (consumed_count < MAX_ITEMS) {
      acquire_sem(full);
      acquire_sem(mutex);

      int item = buffer[out];
      printf("Consumed: %d\n", item);
      out = (out + 1) % BUFFER_SIZE;

      consumed_count++;

      release_sem(mutex);
      release_sem(empty);
   }

   return 0;
}

int main() {
   thread_id producerThread, consumerThread;

   mutex = create_sem(1, "mutex");
   full = create_sem(0, "full");
   empty = create_sem(BUFFER_SIZE, "empty");

   producerThread = spawn_thread(producer, "producer_thread", B_NORMAL_PRIORITY, NULL);
   consumerThread = spawn_thread(consumer, "consumer_thread", B_NORMAL_PRIORITY, NULL);

   resume_thread(producerThread);
   resume_thread(consumerThread);

   wait_for_thread(producerThread, NULL);
   wait_for_thread(consumerThread, NULL);

   delete_sem(mutex);
   delete_sem(full);
   delete_sem(empty);

   return 0;
}
