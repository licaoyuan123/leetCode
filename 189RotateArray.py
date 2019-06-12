class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #Soultions in mind:
        #1 dequeue, pop the last and push in to the head
        #2 Solution extract the last k elements and insert to the head
        #3 
        # for i in range(k):
        #     last= nums.pop()
        #     nums.insert(0, last)
        k = k%len(nums)
        nums[0:] = nums[-k:]+nums[:-k]
            
        
