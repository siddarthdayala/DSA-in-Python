def partition(low, high, arr):
    pivot = arr[high]
    swapIndex = low-1
    for j in range(low, high):
        if pivot > arr[j]:
            swapIndex+=1 
            arr[swapIndex], arr[j] = arr[j], arr[swapIndex]
    arr[swapIndex+1], arr[high] = arr[high], arr[swapIndex+1]
    return swapIndex+1 
    
def quickSort(arr, low, high):
    if low < high:
        p_index = partition(low, high, arr)
        quickSort(arr, low, p_index-1)
        quickSort(arr,p_index+1, high)
        
# Time complexity - O(n^2)
# Space complexity - O(n)

