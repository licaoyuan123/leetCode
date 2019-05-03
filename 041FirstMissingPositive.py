class Solution(object):
    # def swap(self, nums, i,j):
    #     temp=nums[i]
    #     nums[i]=nums[j]
    #     nums[j]=nums[i]
    
    def firstMissingPositive(self, nums):
        """
        #The key is put nums[i] to where it should be located
        :type nums: List[int]
        :rtype: int
        """
        def swap(nums, i,j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
        #Best solution
        i=0
        N = len(nums)
        while i<N:
            if (nums[i]>=1 and nums[i]<N and nums[nums[i]-1]!=nums[i]):
                swap(nums, i, nums[i]-1)
                # temp=nums[i]
                # k=nums[i]-1
                # nums[i]=nums[k]
                # nums[k]=temp
            else:
                i+=1
        j=0
        while j<N:
            if nums[j]!=j+1:
                return j+1
            j+=1
        return N+1
        
        
        # O(n) time
# def firstMissingPositive(self, nums):
#     for i in xrange(len(nums)):
#         while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
#             tmp = nums[i]-1
#             nums[i], nums[tmp] = nums[tmp], nums[i]
#     for i in xrange(len(nums)):
#         if nums[i] != i+1:
#             return i+1
#     return len(nums)+1
    
# O(nlgn) time
# def firstMissingPositive(self, nums):
#     nums.sort()
#     res = 1
#     for num in nums:
#         if num == res:
#             res += 1
#     return res
    
        
        #Solution 1 sort and find the smallest
        #use set to delete duplicated elements
#         result=[]
#         N = len(nums)
#         for i in range(N):
#             if nums[i]>0:
#                 result.append(nums[i])
#         result1=set(result)
        
#         result=list(result1)
#         result.sort()
#         for i in range(len(result)):
#             if result[i]!=i+1:
#                 return i+1
#         return len(result)+1
