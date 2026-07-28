def duplicate(arr):
    n = len(arr)
    arr.sort()
    
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            return True
    return False
    
arr = [1,2,6,3,4,4]
print(duplicate(arr))