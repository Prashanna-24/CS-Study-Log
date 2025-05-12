#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>
#define NUM_PHILOS 5

sem_t chopstick[NUM_PHILOS];

void philo_eat(int n){
    printf("philo %d is eating\n",n);
}

void* philo_fun(void* num){
    int n = *((int*)num);
    if (n == NUM_PHILOS - 1) {
        printf("philo %d wants to eat & tries to take RIGHT chopstick\n", n);
        sem_wait(&chopstick[(n + 1) % NUM_PHILOS]);
        printf("philo %d took RIGHT chopstick\n", n);
        printf("philo %d tries to take LEFT chopstick\n", n);
        sem_wait(&chopstick[n]);
        printf("philo %d took LEFT chopstick\n", n);
    } else {
        printf("philo %d wants to eat & tries to take LEFT chopstick\n", n);
        sem_wait(&chopstick[n]);
        printf("philo %d took LEFT chopstick\n", n);
        printf("philo %d tries to take RIGHT chopstick\n", n);
        sem_wait(&chopstick[(n + 1) % NUM_PHILOS]);
        printf("philo %d took RIGHT chopstick\n", n);
    }
    philo_eat(n);
    sleep(3);
    sem_post(&chopstick[(n+1)%NUM_PHILOS]);
    printf("Philosopher %d leaves the RIGHT chopstick\n",n);
    sem_post(&chopstick[n]);
    printf("Philosopher %d leaves the LEFT chopstick\n",n);
    return NULL;
}


int main(){
    pthread_t T[NUM_PHILOS];
    int indices[NUM_PHILOS];
    for(int i=0;i<NUM_PHILOS;i++){
        sem_init(&chopstick[i],0,1);
    }
    for(int i=0;i<NUM_PHILOS;i++){
        indices[i] = i;
        pthread_create(&T[i],NULL,philo_fun,&indices[i]);
    }
    for(int i=0;i<NUM_PHILOS;i++){
        pthread_join(T[i],NULL);
    }
    for(int i=0;i<NUM_PHILOS;i++){
        sem_destroy(&chopstick[i]);
    }
    return 0;
}
