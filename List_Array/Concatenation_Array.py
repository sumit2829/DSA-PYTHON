def concatenation(arr):
    n = len(arr)
    ans = []
    for i in range(n):
        ans.append(arr[i])
    for i in range(n):
        ans.append(arr[i])
    return ans
arr = [1,4,1,2]
print(concatenation(arr))
    