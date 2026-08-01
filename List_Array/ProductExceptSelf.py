# Brute Force:
'''
def ProductExceptself(arr):
    n = len(arr)
    result = [1] * n
    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= arr[j]
        result[i] = prod
    return result
arr = [1,2,4,6]
print(ProductExceptself(arr))
'''

# Optimal
def ProductExceptself(arr):
    n = len(arr)
    result = [1] * n
    left = 1
    for i in range(n):
        result[i] =  left
        left *= arr[i]
        
    right = 1
    for j in range(n-1,-1,-1):
        result[j] *= right
        right *= arr[j]
    return result
arr = [1,2,4,6]
print(ProductExceptself(arr))

                
                