def binarySearch(arr, length, target):
    low = 0
    high = length-1
    while low<=high:
        mid = low + (high - low)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high = mid-1
        else:
            low = mid+1
    return -1
    


array = [1,2,3,4,5,6,7,8,9]
target = 7

result = binarySearch(array, len(array), target)
if result==-1:
    print(f'{target} is not found in the array')
else:
    print(f'{target} is found at index:{result} in the array')
    
    
    
# Time complexity  -  O(logn)
# Space complexity  -  O(1)
