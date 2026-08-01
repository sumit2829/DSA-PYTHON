# Brute Force
'''
arr = [1,0,1,2]
arr.sort()
print(arr)
'''

# optimal
def color_sort(arr):
    st = 0
    mid = 0
    end = len(arr)-1
    while mid <= end:
        if arr[mid] == 0:
            arr[st], arr[mid] = arr[mid], arr[st]
            st+=1
            mid+=1
        elif arr[mid] == 1:
            mid+=1
        else:
            arr[mid], arr[end] = arr[end], arr[mid]
            end-=1
    return arr
arr = [2,0,2,1,1,0,1,2,0]
print(color_sort(arr))