// Write an MPI program to perform matrix-vector multiplication. The program should distribute the matrix and vector across multiple processes, compute the result in parallel, and gather the final result on the root process.

// The matrix is of size N x N.

// The vector is of size N.

// Use MPI_Scatter to distribute rows of the matrix to each process.

// Use MPI_Gather to collect the result vector on the root process.

// Use MPI_Bcast to broadcast the vector to all processes.

// Use MPI_Reduce to compute the dot product of each row with the vector.


#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

#define N 4  // Size of the matrix and vector

int main(int argc, char** argv) {
    int rank, size;
    int matrix[N][N];  // N x N matrix
    int vector[N];     // N x 1 vector
    int local_row[N];  // Local row for each process
    int local_result;  // Local result for each process
    int result[N];     // Final result vector

    // Initialize MPI
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Check if the number of processes matches the matrix size
    if (size != N) {
        if (rank == 0) {
            printf("Error: Number of processes must be equal to the matrix size (%d).\n", N);
        }
        MPI_Finalize();
        return 1;
    }

    // Root process initializes the matrix and vector
    if (rank == 0) {
        printf("Matrix:\n");
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                matrix[i][j] = i * N + j;  // Fill matrix with sequential values
                printf("%d\t", matrix[i][j]);
            }
            printf("\n");
        }

        printf("\nVector:\n");
        for (int i = 0; i < N; i++) {
            vector[i] = i + 1;  // Fill vector with sequential values
            printf("%d\n", vector[i]);
        }
    }

    // Broadcast the vector to all processes
    MPI_Bcast(vector, N, MPI_INT, 0, MPI_COMM_WORLD);

    // Scatter rows of the matrix to all processes
    MPI_Scatter(matrix, N, MPI_INT, local_row, N, MPI_INT, 0, MPI_COMM_WORLD);

    // Each process computes the dot product of its local row with the vector
    local_result = 0;
    for (int i = 0; i < N; i++) {
        local_result += local_row[i] * vector[i];
    }

    // Gather the results into the root process
    MPI_Gather(&local_result, 1, MPI_INT, result, 1, MPI_INT, 0, MPI_COMM_WORLD);

    // Root process prints the final result
    if (rank == 0) {
        printf("\nResult Vector:\n");
        for (int i = 0; i < N; i++) {
            printf("%d\n", result[i]);
        }
    }

    // Finalize MPI
    MPI_Finalize();
    return 0;
}
