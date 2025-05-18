// RING

#include <stdio.h>
#include "mpi.h"

int main(int argc, char** argv){
    MPI_Init(&argc, &argv);
    int rank, world_size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    int data;
        
    if(rank==0){
        data=123;
    }
    else{
        MPI_Recv(&data, 1, MPI_INT, rank-1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Received data: %d  source:%d  dest:%d\n", data, (rank-1)%world_size, rank);
    }
    MPI_Send(&data, 1, MPI_INT, (rank+1)%world_size, 0, MPI_COMM_WORLD);
    if(rank==0){
        MPI_Recv(&data, 1, MPI_INT, world_size - 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Received data: %d  source:%d  dest:%d\n", data, world_size - 1, rank);
    }
    
    MPI_Finalize();
    return 0;
}
