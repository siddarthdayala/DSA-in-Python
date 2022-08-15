def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        minIndex = i
        j = i+1
        while j<n:
            if arr[j]<arr[i]:
                minIndex = j
            j+=1
        arr[i],arr[minIndex] = arr[minIndex],arr[i]
        
    return arr
    

array = [9,8,7,6,5,4,3,2,1]
print(selectionSort(array))

# Time complexity  -  O(n^2)
# Space complexity  -  O(1)
