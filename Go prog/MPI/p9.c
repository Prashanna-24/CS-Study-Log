#include<stdio.h>
#include <mpi.h>
#define ARRAY_SIZE 9
#define TARGET 3
int main()
{
   int rank,size;
   MPI_Init(NULL,NULL);
   MPI_Comm_rank(MPI_COMM_WORLD, &rank);
   MPI_Comm_size(MPI_COMM_WORLD, &size);
   int arr[] = {2,3,3,3,4,5,6,6,3};
   int local_count, total_count;

   int local_array[ARRAY_SIZE/size];

   MPI_Scatter(arr,ARRAY_SIZE, MPI_INT, local_array, ARRAY_SIZE/size, MPI_INT, 0, MPI_COMM_WORLD);

   printf("Process : %d\n",rank);
   for(int i = 0;i<ARRAY_SIZE/size;i++)
   {
      printf("%d ",local_array[i]);
      if ( == local_array[i])
      {
         local_count++;
      }
   }
   
   MPI_Reduce(&local_count, &total_count, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

   if (rank == 0)
   {
      printf("Count : %d",total_count);
   }

   MPI_Finalize();
   return 0;

}
