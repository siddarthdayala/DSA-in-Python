def linearSearch(array, length, target):
    i = 0
    while i<length:
        if target==array[i]:
            return i
        i+=1
    return -1
    
    
array = [1,32,3,-89,90]
target = -89

result = linearSearch(array, len(array), target)
if result==-1:
    print(f'{target} is not found in the array')
else:
    print(f'{target} is found at index:{result} in the array')
