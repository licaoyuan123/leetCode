class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Binary search find where to insert target and target+1
        
        def search(t):
            lo, hi= 0, len(nums)
            while lo<hi:
                mid = (lo+hi)/2
                if nums[mid]>=t:
                    hi= mid
                else:
                    lo = mid+1
            return lo
        lo = search(target)
        return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]
        


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Let's try to use binary search
        
        result = [-1, -1]
        if(len(nums)==0):
            return result
        
        left,right=0, len(nums)-1
        #Find the left index
        while left<right:
            mid = (left+right)/2
            if nums[mid]<target:
                left = mid+1
            else:
                right = mid
        if nums[left]==target:
            result[0] = left
        else:
            return result
        #Find the right index
        right = len(nums)-1
        while left < right:
            mid = (left+right)/2 +1
            if nums[mid] > target:
                right =  mid-1
            else:
                left = mid
        #if nums[left]==target:
        result[1] = right
        return result
            
        
        
        #Since O(log n), must be binary search
        #However this is a solution of O(n)
        # result = []
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         result.append(i)
        # if len(result)==0:
        #     return [-1,-1]
        # else:
        #     return [result[0], result[-1]]
        
