class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            s,e = i+1, N-1
            while s<e:
                if nums[s]+nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s = s+1
                    while s<e and nums[s] == nums[s-1]:
                        s = s+1
                    while s<e and nums[e-1]==nums[e]:
                        e=e-1
                elif nums[s] + nums[e] < target:
                    s = s+1
                else:
                    e = e-1
        return result
        
        # if len(nums)<3:
        #     return []
        # nums.sort()
        # res=[]
        # for i, v in enumerate(nums[:-2]):
        #     if i>0 and nums[i-1]==v:
        #         continue
        #     l, r= i+1, len(nums)-1
        #     while l<r:
        #         s= v+nums[l]+nums[r]
        #         if s>0:
        #             r-=1
        #         elif s<0:
        #             l+=1
        #         else:
        #             res.append((v, nums[l], nums[r]))
        #             while l<r and nums[l]==nums[l+1]:
        #                 l+=1
        #             while l<r and nums[r]==nums[r-1]:
        #                 r-=1
        #             l+=1; r-=1
        # return res
        
#         if len(nums)<3:
#             return []
#         nums.sort()
#         res = set()
#         for i,v in enumerate(nums[:-2]):
#             if i>=1 and v==nums[i-1]:
#                 continue
#             d={}
#             for x in nums[i+1:]:
#                 if x not in d:
#                     d[-v-x]=1
#                 else:
#                     res.add((v, -v-x, x))
#         return map(list, res)
        
