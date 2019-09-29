class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        left = nums[:]
        
        N = len(nums)
        max_sum = -float("inf")
        current_sum = 0
        for i in range(N):
            if current_sum<0:
                current_sum = nums[i]
            else:
                current_sum+=nums[i]
            left[i] = max_sum = max(max_sum, current_sum)
            
        right = nums[:]
        max_sum = -float("inf")
        current_sum = 0
        
        for i in range(N-1, -1, -1):
            if current_sum<0:
                current_sum = nums[i]
            else:
                current_sum+=nums[i]
            right[i]=max_sum = max(max_sum, current_sum)
        result = -float("inf")
        for i in range(0, N-1):
            result = max(result, left[i]+right[i+1])
        return result
        
        
