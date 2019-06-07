class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = list(set(nums))
        # return len(nums)
        pre = 1
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[pre] = nums[i+1]
                pre+=1
        return pre
                
            
