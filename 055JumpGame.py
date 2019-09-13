class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        #solution 1: greedy:
        if not nums:
            return False
        farthest=nums[0]
        for i in range(1, len(nums)):
            if farthest>=i and nums[i]+i>farthest:
                farthest=nums[i]+i
        return farthest>=len(nums)-1
        
        
        #dp, however O(n**2) calculate backward to make it quicker
        # dp=[False]*len(nums)
        # dp[0]=True
        # for i in range(1, len(nums)):
        #     for j in range(i-1,-1,-1):
        #         if dp[j] and j+nums[j]>=i:
        #             dp[i]=True
        #             break
        # return dp[-1]
        
