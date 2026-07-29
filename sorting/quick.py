def partition(arr, si, ei):
    pivot = arr[ei]      # Last element as pivot
    i = si - 1

    for j in range(si, ei):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot at correct position
    arr[i + 1], arr[ei] = arr[ei], arr[i + 1]

    return i + 1


def quick_sort(arr, si, ei):
    if si < ei:
        p = partition(arr, si, ei)

        quick_sort(arr, si, p - 1)
        quick_sort(arr, p + 1, ei)


arr = [23, 43, 12, 5, 76, 23]
    
quick_sort(arr, 0, len(arr) - 1)

print(arr)