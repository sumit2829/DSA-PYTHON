def linear(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1
        
arr = [12,23,34,11,26,]
target = 11

result = linear(arr, target)

if result != -1:
    print(f"Element fount at index {result}")
else:
    print("Element not fount")