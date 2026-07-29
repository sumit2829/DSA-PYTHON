'''def Two_sum(arr,target):
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1):
            if arr[i]+arr[j] == target:
                return{i,j}
    
arr = [3,4,5,6]
target = 7
print(Two_sum(arr,target)) '''

# Better Approach

def Two_sum(arr,target):
    n = len(arr)
    arr.sort()
    
    l = 0 
    r = n-1
    while(l<=r):
        sum = arr[l]+arr[r]
        if sum == target:
            return {l,r}
        elif target < sum:
            r -=1
        else:
            l +=1
    return {}

arr = [3,5,4,1]
target = 9
print(Two_sum(arr,target))
            
    
