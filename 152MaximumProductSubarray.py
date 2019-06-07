
import numpy as np
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = mini = maxi = nums[0]
        for i in range(1, len(nums)):
            temp0 = mini*nums[i]
            temp1 = maxi * nums[i]
            mini = min(min( temp0 ,temp1 ) , nums[i])
            maxi = max(max( temp0 ,temp1) , nums[i])
            res = max(max(mini, maxi), res)
        return res
        
        
        # for i in range(1, len(nums)):
        #     if nums[i]>0:
        #         maxi= max(maxi*nums[i], nums[i])
        #         mini = min(mini* nums[i], nums[i])
        #     else:
        #         lastmaxi = maxi
        #         maxi = max(mini* nums[i], nums[i])
        #         mini = min(lastmaxi*nums[i], nums[i])
        #     res = max(res, maxi)
        # return res
        
        # res = -float('inf')
        # # product = 1
        # length = len(nums)
        # for i in range(length):
        #     product *= nums[i]
        #     res = max(product, res)
        #     if nums[i] == 0:
        #         product = 1
        # # scan backward
        # product = 1
        # for j in range(length - 1, -1, -1):
        #     product *= nums[j]
        #     res = max(product, res)
        #     if nums[j] == 0:
        #         product = 1
        # return res
    
#My solution Using DP to store the products from the first to the end, however ETL
        #         great = [0]*len(nums)
#         great[0] = nums[0]
#         #cur = []
#         curPre= [nums[0]]
#         for i in range(1, len(nums)):
#             curPre = [j* nums[i] for j in curPre ]
#             curPre.append(nums[i])

#             great[i] = max(curPre)
#             #print(great[i])
#         return max(great)
