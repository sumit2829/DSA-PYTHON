def canEat(arr,k,h):
    n = len(arr)
    hours = 0
    
    for i in range(n):
        hours += (arr[i]+k-1)//k
    return hours <= h

def minEatspeed(arr,h):
    st = 1
    end = max(arr)
    ans = end
    
    while(st <= end):
        mid = st+(end-st)//2
        
        if canEat(arr,mid,h):
            ans = mid
            end = mid-1
        else:
            st = mid+1
    return ans

arr = [1,4,3,2]
h = 9
print(minEatspeed(arr,h))
            
        