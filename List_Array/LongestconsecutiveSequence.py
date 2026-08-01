def longestConsecutive(nums):
    if nums == 0:
        return 0
    nums.sort()
    longest = 1
    curr = 1
    for i in range(len(nums)):
        if nums[i] == nums[i-1]:
            continue
        elif nums[i] == nums[i-1]+1:
            curr +=1
        else:
            curr = 1
        longest = max(longest,curr)
    return longest

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))
            