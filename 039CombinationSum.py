class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target,0, [], res)
        return res
        
        
    def dfs(self, nums, target,index, path, res):
        if target<0:
            return
        if target==0:
            res.append(path)
            return
        for i in xrange(index ,len(nums)):
            if nums[i]>target:
                break
            self.dfs(nums, target- nums[i],i, path+[nums[i]], res )
        
        
#         results=[]
#         re= []
#         for i in range(len(candidates)):
#             if candidates[i]<target:
                
#             if candidates[i]==target:
#                 results.append([target])
#             if candidates[i]>target:
#                 break
#         return results
