#include <stdio.h>
#include <stdlib.h>
#include <OS.h>

sem_id mutex, wrt;
thread_id writerthreads[100], readerthreads[100];
int readercount = 0;

int32 reader(void* param) {
   acquire_sem(mutex);
   readercount++;
   if (readercount == 1) {
      acquire_sem(wrt);
   }
   release_sem(mutex);
   printf("%d reader is inside\n", readercount);
   snooze(3000);
   acquire_sem(mutex);
   readercount--;
   if (readercount == 0) {
      release_sem(wrt);
   }
   release_sem(mutex);
   printf("%d Reader is leaving\n", readercount + 1);
   return 0;
}

int32 writer(void* param) {
   printf("Writer is trying to enter\n");
   acquire_sem(wrt);
   printf("Writer has entered\n");
   release_sem(wrt);
   printf("Writer is leaving\n");
   return 0;
}

int main() {
   int n2, i;
   printf("Enter the number of readers: ");
   scanf("%d", &n2);
   printf("\n");

   mutex = create_sem(1, "mutex");
   wrt = create_sem(1, "wrt");

   for (i = 0; i < n2; i++) {
      writerthreads[i] = spawn_thread(reader, "reader_thread", B_NORMAL_PRIORITY, NULL);
      readerthreads[i] = spawn_thread(writer, "writer_thread", B_NORMAL_PRIORITY, NULL);
   }

   for (i = 0; i < n2; i++) {
      resume_thread(writerthreads[i]);
      resume_thread(readerthreads[i]);
   }

   for (i = 0; i < n2; i++) {
      wait_for_thread(writerthreads[i], NULL);
      wait_for_thread(readerthreads[i], NULL);
   }

   delete_sem(mutex);
   delete_sem(wrt);

   return 0;
}
