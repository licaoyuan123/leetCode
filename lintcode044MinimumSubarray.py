class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        minimum = float("inf")
        current_sum = 0
        for i in range(len(nums)):
            if current_sum>=0:
                current_sum = nums[i]
            else:
                current_sum+=nums[i]
            minimum = min(minimum, current_sum)
        return minimum
        
