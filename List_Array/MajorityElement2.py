def MajorityElement(nums):
    n = len(nums)
    ans = []

    for i in range(n):
        # Skip if already added
        if nums[i] in ans:
            continue

        cnt = 0
        for j in range(n):
            if nums[j] == nums[i]:
                cnt += 1

        if cnt > n // 3:
            ans.append(nums[i])

    return ans


arr = [5, 2, 3, 2, 2, 2, 2, 5, 5, 5]
print(MajorityElement(arr))