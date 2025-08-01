// DYNAMIC MEM ALLOCATION
#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <time.h>

int main(int argc, char **argv) {
    int world_rank, world_size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    int number_amount;

    if (world_rank == 0) {
        const int MAX_NUMBERS = 100;
        int numbers[MAX_NUMBERS];

        // Pick a random amount of integers to send to process one
        srand(time(NULL));
        number_amount = (rand() / (float)RAND_MAX) * MAX_NUMBERS;

        // Fill the numbers array with random integers
        for (int i = 0; i < number_amount; i++) {
            numbers[i] = rand() % 100;  // Random number between 0 and 99
        }

        // Send the random amount of integers to process one
        MPI_Send(numbers, number_amount, MPI_INT, 1, 0, MPI_COMM_WORLD);
        printf("Process 0 sent %d numbers to process 1.\n", number_amount);
    } else if (world_rank == 1) {
        MPI_Status status;

        // Probe for an incoming message from process zero
        MPI_Probe(0, 0, MPI_COMM_WORLD, &status);

        // When probe returns, the status object has the size and other
        // attributes of the incoming message. Get the message size
        MPI_Get_count(&status, MPI_INT, &number_amount);

        // Allocate a buffer to hold the incoming numbers
        int* number_buf = (int*)malloc(sizeof(int) * number_amount);

        // Now receive the message with the allocated buffer
        MPI_Recv(number_buf, number_amount, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Process 1 dynamically received %d numbers from process 0.\n", number_amount);

        // Optionally, print the received numbers
        for (int i = 0; i < number_amount; i++) {
            printf("Received number %d: %d\n", i + 1, number_buf[i]);
        }

        // Free the allocated buffer
        free(number_buf);
    }

    // Finalize the MPI environment
    MPI_Finalize();
    return 0;
}
