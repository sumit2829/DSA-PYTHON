def binary(arr, target):
    st = 0
    end = len(arr) - 1

    while st <= end:
        mid = st + (end - st) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            st = mid + 1
        else:
            end = mid - 1

    return -1


arr = [12, 14, 22, 32, 54, 55]   # Sorted array
target = 22

result = binary(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")