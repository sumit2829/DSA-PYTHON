def removd_duplicate(arr):
    if len(arr) == 0:
        return 0
    
    k = 1
    for i in range(1,len(arr)-1):
        if arr[i] != arr[k-1]:
            arr[k] = arr[i]
            k += 1
    return k
arr = [1,1,2,2,3,4,4]
k = removd_duplicate(arr)
print("k=",k)
print(arr[:k])
        