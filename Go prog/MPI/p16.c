
#include <stdio.h>
#include "mpi.h"
#define N 3

int main(int argc, char** argv){
    int rank, world_size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    int matrix[N][N];
    int vector[N];
    int local_row[N];
    int local_result=0;
    int global_vector[N];

    if (rank == 0) {
        // Initialize the matrix and vector
        int init_matrix[N][N] = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        int init_vector[N] = {1, 2, 3};

        // Copy to matrix and vector
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                matrix[i][j] = init_matrix[i][j];
            }
            vector[i] = init_vector[i];
        }
    }
    
    MPI_Scatter(matrix, N, MPI_INT, local_row, N, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Bcast(vector, N, MPI_INT, 0, MPI_COMM_WORLD);

    printf("local row: ");
    for(int i=0; i<N; i++){
        printf("%d ",local_row[i]);
        local_result = local_result + local_row[i]*vector[i];
    }
    printf("\n");

    MPI_Gather(&local_result, 1, MPI_INT, global_vector, 1, MPI_INT, 0, MPI_COMM_WORLD);

    if(rank==0){
        printf("\nResult Vector:\n");
        for (int i = 0; i < N; i++) {
            printf("%d\n", global_vector[i]);
        }
    }

    MPI_Finalize();
    return 0;

}
