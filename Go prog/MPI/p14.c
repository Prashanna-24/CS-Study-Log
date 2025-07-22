#include<stdio.h>
#include<mpi.h>

int main()
{
   MPI_Init(NULL,NULL);
   int rank,size;
   MPI_Comm_rank(MPI_COMM_WORLD, &rank);
   MPI_Comm_size(MPI_COMM_WORLD, &size);

   int number = 18;
   int dec_value = 3;
   int loser = -1;
   MPI_Status status;

   int rank,size;
   MPI_Comm_rank(MPI_COMM_WORLD,&rank);
   MPI_Comm_size(MPI_COMM_WORLD,&size);

   if (rank == 0)
   {
      MPI_Send(number,1,MPI_INT,(rank+1)%size,TAG_COUNTDOWN, MPI_COMM_WORLD);
   }
   while(1)
   {
      int recv_value;
      // MPI_Recv(
   }
}
