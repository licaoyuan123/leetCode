#However, this solution is TLE or use two much space, let's see if there are better solution

class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum(self, nums, k, target):
        # write your code here
        def Nsum(left, right, target,N, result, results):
            if right-left+1<N or nums[left]*N>target or nums[right]*N<target:
                return
            if N==1:
                for i in range(left, right+1):
                    if i>0 and nums[i]==nums[i-1]:
                        continue
                    if nums[i]==target:
                        results.append(nums[i])
            
            elif N==2:
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
                    if i==left or (i>left and nums[i-1]!=nums[i]  ):
                        Nsum(i+1, right, target-nums[i], N-1, result+[nums[i]], results)
        nums.sort()
        results=[]
        Nsum(0, len(nums)-1, target,k, [],results)
        return len(results)
        
    #     A.sort()
    #     results = []
    #     self.NSum(A, 0, len(A)-1,k, target, [], results)
    #     print(results)
    #     return len(results)
    # def NSum(self, nums, left, right, N,target, result, results):
    #     if right-left+1<N or nums[left]*N>target or nums[right]*N<target:
    #         return
    #     if N==1:
    #         for i in range(left, right+1):
    #             if left>0 and nums[left]==nums[left-1]:
    #                 continue
    #             if nums[i]==target:
    #                 results.append(nums[i])
    #         #return
    #     elif N==2:
    #         while left<right:
    #             sum= nums[left]+nums[right]
    #             if sum==target:
    #                 results.append(result+[nums[left], nums[right]])
    #                 left+=1
    #                 while left<right and nums[left]==nums[left-1]:
    #                     left+=1
    #                 while left<right and nums[right-1]==nums[right]:
    #                     right-=1
                    
    #             elif sum<target:
    #                 left+=1
    #             else:
    #                 right-=1
    #         #return
    #     else:
    #         for i in range(left, right+1):
    #             if i==left or i>0 and nums[i]!=nums[i-1]:
    #                 self.NSum(nums, i+1, right, N-1, target-nums[i], result+[nums[i]], results )
            
