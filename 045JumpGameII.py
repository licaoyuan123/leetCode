class Solution:
    def jump(self, nums: List[int]) -> int:
        start, end, farthest, jump = 0, 0, 0, 0
        for i in range(len(nums)-1):
            farthest= max(farthest, i+nums[i])        
            if farthest>=len(nums)-1:
                jump+=1
                break
            if i==end:
                jump+=1
                end=farthest
                
        return jump
        
#         while end<len(nums)-1:
#             jump+=1
            
#             for i in range(start, end+1):
#                 if i+nums[i]>farthest:
#                     farthest=i+nums[i]
#             start=end
#             end=farthest
#         return jump
            
        
        
        #farthest=nums[0]
        #for i in range(len(nums)):
            
        
        
        # step=[float("inf")]*len(nums)
        # step[0]=0
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if step[j]!=float("inf") and j+nums[j]>=i:
        #             step[i]=min(step[i], step[j]+1)
        # return step[-1]
                    
        
        # step= [float("inf")]*len(nums)
        # step[0]=0
        # for i in range(len(nums)):
        #     for j in range(1,nums[i]+1):
        #         if i+j<len(nums):
        #             if step[i]+1<step[i+j]:
        #                 step[i+j] = step[i]+1
        # return step[-1]
        
