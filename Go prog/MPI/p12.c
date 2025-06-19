#include <stdio.h>
#include<mpi.h>
#define ARRAY_SIZE 12
#define TARGET 2
int main()
{
   MPI_Init(NULL,NULL);
   int rank,size;
   MPI_Comm_rank(MPI_COMM_WORLD,&rank);
   MPI_Comm_size(MPI_COMM_WORLD, &size);

   int arr[ARRAY_SIZE] = {1,2,3,4,5,6,7,2,2,2,2,2};
   int local_array[ARRAY_SIZE/size];

   MPI_Scatter(arr, ARRAY_SIZE/size, MPI_INT, local_array, ARRAY_SIZE/size, MPI_INT, 0, MPI_COMM_WORLD);

   for(int i=0;i<ARRAY_SIZE/size;i++)
   {
      if (TARGET == local_array[i])
      {
         printf("Found in Process %d\n",rank);
      }
   }
   MPI_Finalize();
   return 0;
}
