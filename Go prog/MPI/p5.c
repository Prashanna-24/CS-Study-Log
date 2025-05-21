// COUNTING NO OF 3'S USING SCATTER AND REDUCE

#include <stdio.h>
#include "mpi.h"
#define ARRAY_SIZE 9
#define TARGET 3

int main(int argc, char** argv){
    int rank, size;
    int array[ARRAY_SIZE] = {12,3,2,3,1,2,4,3,3};
    int local_count=0, total_count=0;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int local_array[ARRAY_SIZE/size];

    MPI_Scatter(array, ARRAY_SIZE/size, MPI_INT, local_array, ARRAY_SIZE/size, MPI_INT, 0, MPI_COMM_WORLD);

    printf("process : %d\n", rank);
    for (int i = 0; i < ARRAY_SIZE / size; i++) {
        printf("%d ", local_array[i]);
        if (local_array[i] == TARGET) {
            local_count++;
        }
    }
    printf("\n");

    MPI_Reduce(&local_count, &total_count, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        printf("Total number of 3's in the array: %d\n", total_count);
    }

    MPI_Finalize();
    return 0;
}
