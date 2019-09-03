class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left+1<right:
            mid = left+(right-left)/2
            if nums[mid]==target:
                right=mid
            else:
                if nums[mid]>target:
                    right=mid
                else:
                    left=mid
        if nums[left]==target:
            return left
        if nums[right]==target:
            return right
        return -1
        
        
        
        
        
        
