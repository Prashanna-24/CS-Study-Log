#include <stdio.h>
#include <stdlib.h>

#define MAX_TASKS 10
#define MAX_PRIORITY 5
#define TIME_SLICE 10

// Task structure
typedef struct {
    int id;
    int priority;
    int remaining_time;
} Task;

// Queue structure for each priority level
typedef struct {
    Task* tasks[MAX_TASKS];
    int front;
    int rear;
} Queue;

// Global array of queues for each priority level
Queue priority_queues[MAX_PRIORITY];

// Initialize the queues
void initialize_queues() {
    for (int i = 0; i < MAX_PRIORITY; i++) {
        priority_queues[i].front = -1;
        priority_queues[i].rear = -1;
    }
}

// Enqueue task into the appropriate queue based on priority
void enqueue(Task* task) {
    int priority = task->priority;
    if (priority < 0 || priority >= MAX_PRIORITY) {
        printf("Invalid priority\n");
        return;
    }

    Queue* queue = &priority_queues[priority];
    if (queue->rear == MAX_TASKS - 1) {
        printf("Queue overflow\n");
        return;
    }

    if (queue->front == -1) {
        queue->front = 0;
    }
    queue->rear++;
    queue->tasks[queue->rear] = task;
}

// Dequeue task from the front of the queue
Task* dequeue(int priority) {
    if (priority < 0 || priority >= MAX_PRIORITY) {
        printf("Invalid priority\n");
        return NULL;
    }

    Queue* queue = &priority_queues[priority];
    if (queue->front == -1) {
        printf("Queue underflow\n");
        return NULL;
    }

    Task* task = queue->tasks[queue->front];
    if (queue->front == queue->rear) {
        queue->front = -1;
        queue->rear = -1;
    } else {
        queue->front++;
    }
    return task;
}

// Scheduler function implementing round-robin with priority queue
void schedule() {
    int current_time = 0;

    while (1) {
        for (int i = 0; i < MAX_PRIORITY; i++) {
            Task* task = dequeue(i);
            if (task != NULL) {
                printf("Executing task %d (priority %d) at time %d\n", task->id, task->priority, current_time);
                task->remaining_time -= TIME_SLICE;
                if (task->remaining_time <= 0) {
                    free(task);
                } else {
                    enqueue(task);
                }
            }
        }

        // Check if all queues are empty
        int all_empty = 1;
        for (int i = 0; i < MAX_PRIORITY; i++) {
            if (priority_queues[i].front != -1) {
                all_empty = 0;
                break;
            }
        }

        if (all_empty) {
            break;
        }

        current_time += TIME_SLICE;
    }
}


int main() {
    initialize_queues();

    // Example tasks
    for (int i = 0; i < MAX_TASKS; i++) {
        Task* task = (Task*)malloc(sizeof(Task));
        task->id = i + 1;
        task->priority = rand() % MAX_PRIORITY; // Random priority
        task->remaining_time = rand() % 50 + 10; // Random remaining time
        enqueue(task);
    }

    // Run the scheduler
    schedule();

    return 0;
}