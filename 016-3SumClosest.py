"""
I think the insight is something like this - 
Given an array and a brute force algorithm that seems way too slow (n^3), 
try to think of ways that we could get it to n^2, nlogn, n. 
If the given array problem is the type of a problem where order/index doesn't matter, 
always consider sorting the array. Once you've got it sorted, you have a great heuristic to use to iterate over the array.
If you've gotten to that point, and are wondering how to traverse the array,
1, 2, 3+ pointers is always something that should be at the top of your list of things to consider when tackling an unfamiliar problem.
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # nums.sort()
        # mini = float('inf')
        # sumArray = []
        # for i in range(len(nums)-2):
        #     left, right =i+1, len(nums)-1
        #     while left< right:
        #         s = nums[i]+nums[left]+nums[right]
        #         if s==target:
        #             return s
        #         sumArray.append(s)
        #         if s< target:
        #             left+=1
        #         else:
        #             right-=1
        # mini = float('inf')
        # res = 0
        # for i in range(len(sumArray)):
        #     if abs(sumArray[i]-target)<mini:
        #         mini = abs(sumArray[i]-target)
        #         res = sumArray[i]
        # return res
            
            
                
                #sums.append(s)
                # if abs(s- target)<abs(result-target ):
                #     result = s
                # if s<target:
                #     left+=1
                # elif s>target:
                #     right-=1
#         return result
        
        
        nums.sort()
        result = float('inf')
        for i in range(len(nums)-2):
            left, right =i+1, len(nums)-1
            while left< right:
                s = nums[i]+nums[left]+nums[right]
                if s==target:
                    return s
                #sums.append(s)
                if abs(s- target)<abs(result-target ):
                    result = s
                if s<target:
                    left+=1
                elif s>target:
                    right-=1
        return result
    
    
#         mini = float('inf')
#         res = 0
#         for i in range(len(sums)):
#             if abs(sums[i]-target)<mini:
#                 mini = abs(sums[i]-target)
#                 res = sums[i]

#         return res
        
                    

        
        
        
        
        #First solution however it's TLE, O(n^3)
        #Since the result may not be conjugance, sort is useless
        #nums.sort()
        # res = float('inf')
        # resSum = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             s= nums[i]+nums[j]+ nums[k]
        #             cur = target- s
        #             if abs(cur)<res:
        #                 res = abs(cur)
        #                 resSum = s
        # return resSum
        
        
        #Wrong solution below
        #         dis = []
#         for i in range(len(nums)-2):
#             left,right = i+1, len(nums)-1
#             while left<right:
#                 dis.append(nums[i]+nums[left]+nums[right])
#                 left+=1
#                 dis.append(nums[i]+nums[left]+nums[right])
#                 right-=1
#         mini = float('inf')
#         res = 0
#         for i in range(len(dis)):
#             if abs(dis[i])<mini:
#                 mini = abs(dis[i])
#                 res = dis[i]

#         return res
        
        
#     def des(self, a,b):
#         return abs(a-b)
