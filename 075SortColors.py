class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=len(nums)-1
        zero=0
        
        while left<=right:
            if nums[left]==0:
                nums[left], nums[zero] = nums[zero], nums[left]
                zero+=1
                left+=1
            
            elif nums[left]==2:
                nums[left], nums[right] = nums[right], nums[left]
                right-=1
            else:
                left+=1
        
        
        
        # left = 0
        # right=len(nums)-1
        # while left<=right:
        #     while left<=right and nums[left]==0:
        #         left+=1
        #     while left<=right and nums[right]!=0:
        #         right-=1
        #     if left<=right:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left+=1
        #         right-=1
        # right= len(nums)-1
        # while left<=right:
        #     while left<=right and nums[left]==1:
        #         left+=1
        #     while left<=right and nums[right]!=1:
        #         right-=1
        #     if left<=right:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left+=1
        #         right-=1
        
        
        
        
        
        
        
        #dic={0:0, 1:0, 2:0}
        # for i in nums:
        #     dic[i]+=1
        # result=[]
        # for i in range(3):
        #     print(dic[i])
        #     for j in range(dic[i]):
        #         result.append(i)
        # for i in range(len(nums)):
        #     nums[i] = result[i]
        
