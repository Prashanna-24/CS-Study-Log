#include<stdio.h>
#include <mpi.h>

int main(int argc, char* argv)
{
   int rank,size;
   int a,b,c;
   MPI_Init(NULL,NULL);
   MPI_Comm_rank(MPI_COMM_WORLD, &rank);
   MPI_Comm_size(MPI_COMM_WORLD, &size);

   if (rank == 0)
   {
      printf("Enter a : ");
      fflush(stdout);
      scanf("%d",&a);
      printf("Enter b : ");
      fflush(stdout);
      scanf("%d",&b);
   }

   MPI_Bcast(&a, 1, MPI_INT, 0, MPI_COMM_WORLD);
   MPI_Bcast(&b, 1, MPI_INT, 0, MPI_COMM_WORLD);

   c = a + b;
   printf("Hello. I am %d of %d, result is %d", rank, size, c);

   MPI_Barrier(MPI_COMM_WORLD);
   MPI_Finalize();
   return 0; 
}
