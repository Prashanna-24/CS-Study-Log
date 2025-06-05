// MIN AND SUM USING SEND AND RECV

#include <limits.h>
#include "mpi.h"

#define ARRAY_SIZE 9

int main(int argc, char** argv) {
    int rank, size;
    int array[ARRAY_SIZE] = {12, 3, 2, 3, 1, 2, 4, 3, 3};
    int local_sum = 0, local_min = INT_MAX;
    int global_sum = 0, global_min = INT_MAX;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Calculate the range of indices each process will work on
    int chunk_size = ARRAY_SIZE / size;
    int start_index = rank * chunk_size;
    int end_index = (rank == size - 1) ? ARRAY_SIZE : (rank + 1) * chunk_size;

    // Each process computes local sum and local minimum
    for (int i = start_index; i < end_index; i++) {
        local_sum += array[i];
        if (array[i] < local_min) {
            local_min = array[i];
        }
    }

    printf("Process %d: Local Sum = %d, Local Min = %d\n", rank, local_sum, local_min);

    // Rank 0 will gather the results from all processes
    if (rank == 0) {
        global_sum = local_sum;
        global_min = local_min;
        int temp_sum, temp_min;

        // Receive results from other processes
        for (int i = 1; i < size; i++) {
            MPI_Recv(&temp_sum, 1, MPI_INT, i, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            MPI_Recv(&temp_min, 1, MPI_INT, i, 1, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

            global_sum += temp_sum;
            if (temp_min < global_min) {
                global_min = temp_min;
            }
        }

        printf("Global Sum = %d\n", global_sum);
        printf("Global Min = %d\n", global_min);
    } else {
        // Send local results to process 0
        MPI_Send(&local_sum, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
        MPI_Send(&local_min, 1, MPI_INT, 0, 1, MPI_COMM_WORLD);
    }

    MPI_Finalize();
    return 0;
}
