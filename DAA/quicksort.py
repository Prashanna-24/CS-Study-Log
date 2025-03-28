# Function to find the partition position
def partition(array, low, high):
   pivot = array[high]
   # pointer for greater element
   i = low - 1
   # compare each element with pivot
   for j in range(low, high):
      if array[j] <= pivot:
         # If element smaller than pivot is found
         # swap it with the greater element pointed by i
         i = i + 1
         (array[i], array[j]) = (array[j], array[i])

   # Swap the pivot element with the greater element specified by i
   (array[i + 1], array[high]) = (array[high], array[i + 1]) 
   # Return the position from where partition is done
   return i + 1

def quickSort(array, low, high):
   if low < high:
      pi = partition(array, low, high)
      # Recursive call on the left of pivot
      quickSort(array, low, pi - 1)
      # Recursive call on the right of pivot
      quickSort(array, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)