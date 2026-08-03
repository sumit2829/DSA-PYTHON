def peakIdx(nums):
    st = 1
    end = len(nums)-2
    
    while st <= end:
        mid = st+(end-st)//2
        
        if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid-1] < nums[mid]:
            st = mid+1
        else:
            end = mid-1
    return -1

nums =[0,2,5,3,1]
print(peakIdx(nums))