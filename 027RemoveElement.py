class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #Solution0:
        while val in nums:
            nums.remove(val)
        return len(nums)
        
        
        
#Solution 1 swap the items to be deleted to the end of the array
        # left, right =0, len(nums)-1
        # while left <=right:
        #     if nums[left]==val:
        #         nums[left], nums[right], right = nums[right], nums[left], right-1
        #     else:
        #         left+=1
        # return left
    
    
    
   
        
