class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #Find the last less than target
        if not nums:
            return 0
        
        start, end = 0, len(nums)-1
        while start+1<end:
            mid = start+(end-start)/2
            
            if nums[mid]==target:
                return mid
                #end=mid
            else:
                if nums[mid]>target:
                    end=mid
                else:
                    start=mid
        if nums[end]<target:
            return end+1
        if nums[start]<target:
            return start+1
        else:
            return start


#Shows how to write a correct binary search algorithm
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        """
        
        left = 0
        right = len(nums)-1
        
        while left<=right:
            #mid =left+ (right - left)/2
            mid = (left+right)/2
            if nums[mid]>=target:
                right= mid - 1
            else:
                left=mid + 1
        return left
        
        
        
        
        #Binary Search or Brute Search
        
        #Solution 1 faster than 79.24%
        # if target in nums:
        #     for i in range(len(nums)):
        #         if nums[i]==target:
        #             return i
        # else:
        #     flag=False
        #     for i in range(len(nums)):
        #         if nums[i]>target:
        #             flag=True
        #             return i
        #     if not flag:
        #         return len(nums)
