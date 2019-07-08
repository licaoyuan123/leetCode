class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.dfs(candidates,target, 0, [], res)
        return res
    def dfs(self, nums,target, index, path, res):
        if target<0:
            return
        if target==0:
            res.append(path)
            return
        for i in xrange(index, len(nums)):
            # while i+1<len(nums) and nums[i]==nums[i+1]:
            #     i+=1
            if i>index and nums[i]==nums[i-1]:
                continue
            self.dfs(nums, target-nums[i], i+1, path +[nums[i]], res )
        
