"""@package docstring
Documentation for this module.

Algorithm details to follow:
1. Choose a pivot
2. Set a left pointer and right pointer
3. Compare the left pointer element (lelement) with the pivot and the right pointer element (relement) with the pivot.
4. Check if L element < pivot and R element > pivot:
    4.1 If yes, increment the left pointer and decrement the right pointer
    4.2 If not, swap the L element and R element
5. When left >= right, swap the pivot with either left or right pointer.
6. Repeat steps 1 - 5 on the left half and the right half of the list till the entire list is sorted.

More details.
""" 

## \brief Initial call to execute_quicksort on array as a whole
# \param arr - array to apply quick sort on
def quickSort(arr):
    execute_quicksort(arr, 0, len(arr)-1)

## \brief helper function to run partition method and recursively call helper function
# \param arr - array currently sorting
# \param first - start of current array or split array (when partitioned)
# \param end - end of current array or split array (when partitioned)
def execute_quicksort(arr, start, end):
    if start < end:
        split = partition(arr,start,end)
        execute_quicksort(arr, start, split-1)
        execute_quicksort(arr, split+1, end)


## \brief Compare pivot element to swap
# This function will compre the pivot element against left and right elements to swap or modify L/R pointer
# if L element < pivot and R element > pivot:
# If yes, increment the left pointer and decrement the right pointer
# Else, swap the L element and R element
# When left >= right, swap the pivot with either left or right pointer.
# \param arr - array currently sorting
# \param left - defines left pointer in array
# \param right - defines right pointer in array
def partition(arr, start, right):

    pivotvalue = arr[start]
    left = start+1

    while True:
        while arr[right] >= pivotvalue and right >= left:
            right -= 1

        while left <= right and arr[left] <= pivotvalue:
            left += 1

        if right < left:
            break
        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

    temp = arr[start]
    arr[start] = arr[right]
    arr[right] = temp

    return right



if __name__ == '__main__':
    arr = [64,76,23,19,80,25,34,25,200]
    quickSort(arr)
    print(arr)
