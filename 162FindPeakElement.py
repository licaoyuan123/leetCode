class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #binary search
        start, end = 0, len(nums)-1
        while start+1<end:
            mid=start+(end-start)/2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            if nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
                end=mid
            else:
                if nums[mid-1]<nums[mid] and nums[mid]<nums[mid+1]:
                    start=mid
                else:
                    end=mid
        if nums[start]>nums[end]:
            return start
        return end
