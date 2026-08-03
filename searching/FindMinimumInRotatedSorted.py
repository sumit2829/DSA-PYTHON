# Brute force:
'''
def findmin(nums):
    mn = nums[0]
    for num in nums:
        mn = min(mn,num)
    return mn
nums = nums = [4,5,6,7,0,1,2]
print(findmin(nums))
'''

# optimal:

def findmin(nums):
    st = 0
    end = len(nums)-1
    
    while st < end:
        mid = st+(end-st)//2
        
        if nums[mid] > nums[end]:
            st = mid+1
        else:
            end = mid
    return nums[st]

nums = [4,5,6,7,0,1,2]
print(findmin(nums))