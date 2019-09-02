class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res=[]
        def dfs(nums, position,current, res):
            if position==len(nums):
                res.append(current)
                return
            dfs(nums, position+1, current, res)
            dfs(nums, position+1, current+[nums[position]], res)
            
        dfs(nums, 0,[], res)
        return res
                
        



class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums,0, [],res)
        return res
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path +[nums[i]],res)
        
        
