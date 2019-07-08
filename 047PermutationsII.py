class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        def dfs(nums, path, res):
            if len(nums)==0:
                res.append(path)
                return
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                dfs(nums[:i]+nums[i+1:], path+[nums[i]], res )
            
        res = []
        dfs(nums, [], res)
        return res
        
