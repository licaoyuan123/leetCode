#Best Solution:

class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # write your code here
        #Solution 3
        N=len(A)
        left=0
        right=N-1
        while left<=right:
            while left<=right and A[left]<0:
                left+=1
            while left<=right and A[right]>0:
                right-=1
            if left<right:
                A[left], A[right] =A[right], A[left]
                left+=1
                right-=1
        negative_num = left
        positive_num = N-negative_num
        if negative_num>=positive_num:
            left=1
        else:
            left=0
        if positive_num>=negative_num:
            right=N-2
        else:
            right=N-1
        while left<=right:
            A[left], A[right] = A[right], A[left]
            left+=2
            right-=2


class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # write your code here
        #Solution 2
        N = len(A)
        positive =0
        for i in range(N):
            if A[i]>0:
                positive+=1
        negative = N-positive
        left=0
        right =N-1
        if positive>negative:
            while left<right:
                while left<right and A[left]>0:
                    left+=1
                while left<right and A[right]<0:
                    right-=1
                if left<=right:
                    A[left], A[right] = A[right], A[left]
                    left+=1
                    right-=1
            left=1
            right = N-1
            while left<right:
                A[left], A[right] = A[right], A[left]
                left+=2
                right-=2
        else:
            while left<right:
                while left<right and A[left]<0:
                    left+=1
                while left<right and A[right]>0:
                    right-=1
                if left<=right:
                    A[left], A[right] = A[right], A[left]
                    left+=1
                    right-=1
            #left=0
            if positive==negative:
                left, right = 1, len(A)-2
            else:
                left, right=1, len(A)-1
            while left<right:
                A[left], A[right] = A[right], A[left]
                left += 2
                right -= 2

        
        
        
        
    #     nums_positive = [i for i in A if i>0]
    #     nums_negative = [i for i in A if i<0]
    #     if len(nums_positive)>len(nums_negative):
    #         nums = self.helper(nums_positive, nums_negative)
    #     else:
    #         nums = self.helper(nums_negative, nums_positive)
        
    #     for i in range(len(nums)):
    #         A[i] = nums[i]
    # def helper(self, nums_first, nums_second):
    #     nums=[]
    #     for i in range(len(nums_second)):
    #         nums.append(nums_first[i])
    #         nums.append(nums_second[i])
    #     if len(nums_first)>len(nums_second):
    #         nums.append(nums_first[-1])
    #     return nums
        
        
