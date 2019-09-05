class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = nums[-1]
        start, end = 0, len(nums)-1
        while start+1<end:
            mid = start+(end-start)/2
            
            if nums[mid]==target:
                end = mid
            else:
                if nums[mid]>target:
                    start=mid
                else:
                    end=mid
        return min(nums[start], nums[end])
        # if nums[start]<=target:
        #     return nums[start]
        # else:
        #     return nums[end]
        
