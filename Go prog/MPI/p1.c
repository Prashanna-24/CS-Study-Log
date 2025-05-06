#include <stdio.h>
#include "mpi.h"

int main(int argc, char* argv[])
{
    int rank, size;
    int a, b, c;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Only the master process (rank 0) will read the input
    if (rank == 0) {
        printf("Enter a: ");
        fflush(stdout); // Flush the output buffer
        scanf("%d", &a);
        printf("Enter b: ");
        fflush(stdout); // Flush the output buffer
        scanf("%d", &b);
    }

    // Broadcast the values of a and b to all processes
    MPI_Bcast(&a, 1, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Bcast(&b, 1, MPI_INT, 0, MPI_COMM_WORLD);

    // Each process calculates the sum
    c = a + b;

    // Print the result from each process
    printf("Hello, world, I am %d of %d, my result is %d\n", rank, size, c);
    printf("Process %d Exists\n", rank);

    MPI_Barrier(MPI_COMM_WORLD);
    MPI_Finalize();
    return 0;
}
