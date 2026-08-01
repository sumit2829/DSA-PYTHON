def firstmissing(nums):
    n = len(nums)

    # Check every positive number from 1 to n
    for i in range(1, n + 1):
        found = False

        for j in range(n):
            if nums[j] == i:
                found = True
                break

        if not found:
            return i

    return n + 1


nums = [-2, -1, 0]
nums = [1,2,4]
print(firstmissing(nums))