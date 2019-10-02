class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum=0
        result = 0
        #dic={0:1}
        dic={}
        for i in range(len(nums)):
            sum+=nums[i]
            if sum-k in dic:
                result+=dic[sum-k]
            if sum==k:
                result+=1
            if sum in dic:
                dic[sum]+=1
            else:
                dic[sum] = 1
        return result
        
