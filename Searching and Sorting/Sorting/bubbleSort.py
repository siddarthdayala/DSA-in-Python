def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

array = [9,7,6,5,4,3]
print(bubbleSort(array))

# Time complexity  -  O(n^2)
# Space complexity  -  O(1)
