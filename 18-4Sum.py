#This solution is actually N sum
#credit to @zhuyinghua1203 https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def Nsum(left, right, target,N, result, results):
            if right-left+1<N or nums[left]*N>target or nums[right]*N<target or N<2:
                return
            if N==2:
                #if nu
                while left<right:
                    s = nums[left]+nums[right]
                    if s==target:
                        results.append(result + [nums[left], nums[right]] )
                        
                        left+=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                    elif s<target:
                        left+=1
                    else:
                        right-=1
                
            else:
                for i in range(left, right+1):
                    #With out this line, the answer will be error
                    if i==left or (i>left and nums[i-1]!=nums[i]  ):
                        Nsum(i+1, right, target-nums[i], N-1, result+[nums[i]], results)
        nums.sort()
        results=[]
        N=4
        Nsum(0, len(nums)-1, target,N, [],results)
        return results
            
            
        
