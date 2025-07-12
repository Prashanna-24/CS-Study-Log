#include<stdio.h>
#include<mpi.h>
#define ARRAY_SIZE 12
int main()
{
   MPI_Init(NULL,NULL);
   int rank,size;
   MPI_Comm_rank(MPI_COMM_WORLD, &rank);
   MPI_Comm_size(MPI_COMM_WORLD, &size);
   int chunk_size = ARRAY_SIZE/size;
   int local_array[chunk_size];
   int arr[ARRAY_SIZE] = {0,1,9,2,8,3,7,4,6,5,-2,-25};
   
   MPI_Scatter(arr,chunk_size,MPI_INT,local_array,chunk_size, MPI_INT,0,MPI_COMM_WORLD);

   int local_min = local_array[0];
   for(int i = 1;i<chunk_size;i++)
   {
      if (local_array[i] < local_min)
      {
         local_min = local_array[i];
      }
   }
   int gather_min[size];
   MPI_Gather(&local_min, 1, MPI_INT, gather_min, 1, MPI_INT, 0,MPI_COMM_WORLD);

   int min;
   if (rank == 0)
   {
      min = gather_min[0];
      for(int i = 1;i<size;i++)
      {
         if(gather_min[i] < min)
         {
            min = gather_min[i];
         }
      }
      printf("Minimum of the array is %d\n", min);
   }
   
   MPI_Finalize();
   return 0;

}
