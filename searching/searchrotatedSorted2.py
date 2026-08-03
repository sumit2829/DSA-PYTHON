# search Rotated Sorted list/Array 2.
def search(nums,target):
    st = 0
    end = len(nums)-1
    
    while st <= end:
        mid = st+(end-st)//2
        
        if nums[mid] == target:
            return True
        
        # Not decided the sorted part
        if nums[st] == nums[mid] and nums[mid] == nums[end]:
            st+=1
            end-=1
        
        # left part sorted
        elif nums[st] <= nums[mid]:
            if target >= nums[st] and target <= nums[mid]:
                end = mid-1
            else:
                st = mid+1
        else:
            # right part sorted
            if target > nums[mid] and target <= nums[end]:
                st = mid+1
            else:
                end = mid-1
    return False
    
nums = [2,5,6,0,0,1,1,2]
target = 99
print(search(nums,target))
            
            
