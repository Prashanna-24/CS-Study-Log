// PING PONG

#include <mpi.h>
#include <stdio.h>

#define PING_PONG_LIMIT 4

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    int ping_pong_count = 0;
    int partner_rank = (world_rank + 1) % 2;

    while (ping_pong_count < PING_PONG_LIMIT) {
        if (world_rank == ping_pong_count % 2) {
            // Increment and send
            ping_pong_count++;
            MPI_Send(&ping_pong_count, 1, MPI_INT, partner_rank, 0, MPI_COMM_WORLD);
            printf("SENT - ping count: %d  source: %d   dest: %d\n", ping_pong_count, world_rank, partner_rank);
        } else {
            // Receive and log
            MPI_Recv(&ping_pong_count, 1, MPI_INT, partner_rank, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            printf("RECEIVED - ping count: %d  source: %d   dest: %d\n", ping_pong_count, partner_rank, world_rank);
        }
    }

    MPI_Finalize();
    return 0;
}
