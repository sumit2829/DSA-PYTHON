''''
def majority_element(arr):
    n = len(arr)
    
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] == arr[i]:
                count +=1
        if count > n/2:
            return arr[i]
    return -1
arr = [5,5,1,1,1,5,5]
print(majority_element(arr))
'''

#  Optimal
def majority_element(arr):
    count = 0
    candidate = None
    for x in arr:
        if count == 0:
            candidate = x
        if x == candidate:
            count +=1
        else:
            count -=1
    return candidate

arr = [5,5,1,1,1,5,5]
print(majority_element(arr))
        
        