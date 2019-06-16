class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def swap(nums, i, j):
            temp = nums[j]
            nums[j] = nums[i]
            nums[i]= temp
        def reverse(nums, i):
            j = len(nums)-1
            while i<j:
                swap(nums, i, j)
                i+=1
                j-=1
        
        N = len(nums)-1
        i=N-1
        while i>=0 and nums[i+1]<=nums[i]:
            i-=1
        if i>=0:
            j= N
            while nums[j]<=nums[i]:
                j-=1
            swap(nums, i, j)
        reverse(nums, i+1)
            
#             if nums[i]<nums[i+1]:
#                 break
#             i-=1
#         if i>=0:
#             j=N
#             if nums[j]<=nums[i]:
#                 j-=1            
#             swap(nums, i, j)
            
#         reverse(nums, i+1)
        
        
