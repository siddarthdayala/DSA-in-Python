def merge(left,right):
    if not right:
        return left
    elif not left:
        return right
    l_ind = r_ind = 0
    result = []
    while len(result) < len(left) + len(right):
        if left[l_ind]<=right[r_ind]:
            result.append(left[l_ind])
            l_ind+=1 
        else:
            result.append(right[r_ind])
            r_ind+=1 
        
        if l_ind==len(left):
            result+=right[r_ind:]
            break
        elif r_ind==len(right):
            result+=left[l_ind:]
            break
            
    return result
        
def mergeSort(listt):
    if len(listt) < 2:
        return listt
    mid = len(listt)//2
    return merge(mergeSort(listt[:mid]), mergeSort(listt[mid:]))
    
    
Time Complexity - O(nlogn)
Space Complexity - O(n)
