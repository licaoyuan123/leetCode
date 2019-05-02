class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#Solution 1, O(n)
        count=1
        N=len(nums)
        major= nums[0]
        for i in range(1,N):
            if nums[i]==major:
                count+=1
            else:
                count-=1
            if(count==0):
                count+=1
                major=nums[i]
        return major
        
        
#Solution 2 sort and take the middle, O(nlogn)        
#         nums.sort()
#         return nums[len(nums)/2]
        
    
