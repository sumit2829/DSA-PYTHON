def remove(arr,val):
    n = len(arr)
    
    k = 0
    for i in range(n):
        if arr[i] != val:
            arr[k] = arr[i]
            k +=1
    return k

arr =[2,3,4,5,5,6]
val = 2

k = remove(arr, val)
print(k)
print(arr[:k])

