// MINIMUM OF ARRAY

#include <stdio.h>
#include "mpi.h"
#define ARRAY_SIZE 9

int main(int argc, char** argv){
    int rank, size;
    int array[ARRAY_SIZE] = {12,3,2,3,1,2,4,3,3};
    int local_min=0, global_min=0;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int local_array[ARRAY_SIZE/size];

    MPI_Scatter(array, ARRAY_SIZE/size, MPI_INT, local_array, ARRAY_SIZE/size, MPI_INT, 0, MPI_COMM_WORLD);

    printf("process : %d\n", rank);
    local_min = local_array[0];
    for (int i = 0; i < ARRAY_SIZE / size; i++) {
        printf("%d ", local_array[i]);
        if (local_array[i] < local_min) {
            local_min = local_array[i];
        }
    }
    printf("\n");

    MPI_Reduce(&local_min, &global_min, 1, MPI_INT, MPI_MIN, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        printf("global min: %d\n", global_min);
    }

    MPI_Finalize();
    return 0;
}
