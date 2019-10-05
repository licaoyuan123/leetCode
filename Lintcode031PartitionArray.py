class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        N = len(nums)
        if N==0 or N==1:
            return 0
        left=0
        right = N-1
        while left<=right:
            while left<=right and nums[left]<k:
                left+=1
            
            while left<=right and nums[right]>=k:
                right-=1
            
            if left<=right:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
        return left
        # if nums[right]>=k:
        #     return right
        # else:
        #     return right+1
