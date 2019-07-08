class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        self.dfs(nums, [], res)
        return res
    def dfs(self,nums,  path, res):
        if not nums:
            res.append(path)
        
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
            
#             for j in range(0, len(nums)):
#                 self.dfs(nums, i+1, path+[nums[j]], res)
        
        
