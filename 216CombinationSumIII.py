class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        result = []
        self.search(nums, n, 0, k, [], result)
        return result
    
    def search(self, nums, target, index, k, path, result):
        
        if target<0:
            return
        if len(path)==k:
            if target==0:
                result.append(path)
            return
        for i in range(index, len(nums)):
            if nums[i]>target:
                break
            self.search(nums, target-nums[i], i+1, k, path+[nums[i]], result)
        
