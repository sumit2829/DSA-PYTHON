# Brute force

""" def insert_element(arr, target):
    n = len(arr)
    
    for i in range(n):
        if arr[i] >= target:
            return i
    return arr.size()

arr = [1,2,4,5]
target = 2
print(insert_element(arr,target))
"""

# optimal 
def insert(arr,target):
    n = len(arr)-1
    
    st = 0
    end = n
    
    ans = n
    
    while(st < end):
        mid = st+(end-st)//2
        
        if arr[mid] >= target:
            ans = mid
            end = mid-1
        else:
            st = mid+1
    return ans

arr = [1,2,4,5,9]
target = 7
print(insert(arr,target))