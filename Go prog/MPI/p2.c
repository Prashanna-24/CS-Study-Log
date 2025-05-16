#include "mpi.h"
#include <stdio.h>

int main(int argc, char *argv[]) {
    int rank, size, i;
    int buffer[10];
    MPI_Status status;

    MPI_Init(&argc, &argv); 
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (size < 2) {
        printf("Please run with two processes.\n");
        fflush(stdout);
        MPI_Finalize();
        return 0;
    }

    if (rank == 0) { // Sender process
        for (i = 0; i < 10; i++) {
            buffer[i] = i; // Initialize buffer with values 0 to 9
        }
        MPI_Ssend(buffer, 10, MPI_INT, 1, 123, MPI_COMM_WORLD); // synch Send buffer to rank 1
    }

    if (rank == 1) { // Receiver process
        for (i = 0; i < 10; i++) {
            buffer[i] = -1; // Initialize buffer with -1
        }
        MPI_Recv(buffer, 10, MPI_INT, 0, 123, MPI_COMM_WORLD, &status); // Receive data from rank 0
        for (i = 0; i < 10; i++) {
            printf("%d\t", buffer[i]); // Print received data
            if (buffer[i] != i) {
                printf("Error: buffer[%d] = %d but is expected to be %d\n", i, buffer[i], i);
            }
        }
        fflush(stdout); // Flush output to console
    }

    MPI_Finalize(); // Clean up MPI
    return 0;
}
