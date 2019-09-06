
#solution 1 binary search twice
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        root=self.findroot(nums)
        if target>nums[-1]:
            return self.binarysearch(nums, target, 0, root)
        else:
            return self.binarysearch(nums, target, root, len(nums)-1)
    
    
    
    def binarysearch(self, nums: List[int], target:int, left: int, right:int) ->int:
        #left, right=0, len(nums)-1
        #target = nums[-1]
        while left+1<right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            else:
                if nums[mid]>target:
                    right = mid
                else:
                    left=mid
        if nums[left]==target:
            return left
        if nums[right]==target:
            return right
        return -1
        
    def findroot(self, nums: List[int]) -> int:
        left, right=0, len(nums)-1
        target = nums[-1]
        while left+1<right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            else:
                if nums[mid]>target:
                    left = mid
                else:
                    right=mid
        if nums[left]<nums[right]:
            return left
        else:
            return right
