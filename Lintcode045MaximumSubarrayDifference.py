class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """
    def maxDiffSubArrays(self, nums):
        # write your code here
        N = len(nums)
        if N<2:
            return None
        if N==2:
            return abs(nums[0] - nums[1])
        big_left = [0]*N
        # big_left[0] = nums[0]
        big_right = [0]*N
        # big_right[-1] = nums[-1]
        small_left = [0]*N
        # small_left[0] = nums[0]
        small_right = [0]*N
        # small_right[-1] = nums[-1]
        sum_left = -float("inf")
        for i in range(N):
            big_left[i]=sum_left = max(nums[i], sum_left+nums[i])
        
        sum_right = -float("inf")
        for i in range(N-1, -1, -1):
            big_right[i] = sum_right = max(nums[i], sum_right+nums[i])
        
        sum_left = float("inf")
        for i in range(N):
            small_left[i] = sum_left = min(nums[i], nums[i]+sum_left)
        sum_right = float("inf")
        for i in range(N-1, -1, -1):
            small_right[i] = sum_right = min(nums[i], nums[i] +sum_right)
        first= [0]*(N-1)
        second = [0]*(N-1)
        for i in range(1, N):
            first[i-1] = abs(big_left[i-1] - small_right[i])
        for i in range(1, N):
            second[i-1]  =abs(small_left[i-1] - big_right[i])
        return max(max(first), max(second))
