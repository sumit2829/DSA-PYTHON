# Brute Force 

'''def sqrt(x):
    if x == 0: return 0
    if x == 1: return 1
    
    for i in range(x):
        if i*i > x:
            return i-1
        return 0
x = int(input("Enter number: "))
print(sqrt(x))    
    '''
    
# optimal

def sqrt(x):
    if x == 0: return 0
    
    st = 1
    end = x
    ans = 0
    
    while(st <= end):
        mid = st+(end-st)//2
        if mid*mid == x:
            return mid
        elif mid*mid > x:
            ans = mid
            end = mid-1
        else:
            st = mid+1
    return ans
    
x = int(input("Enter Number: "))
print(sqrt(x))