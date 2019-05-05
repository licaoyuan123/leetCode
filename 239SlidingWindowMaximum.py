#I have totally forget how to solve it half year later, however, I saw and tried some more smarter solutions
from Queue import PriorityQueue
from collections import deque
class Solution(object):
    def findMax(self, pq, start):
        while True:
            value, index = pq.get()
            if index>=start:
                pq.put((value, index))
                return (value,index)
    def add_to_deq(self,dq, nums, index):
        while len(dq) and nums[index]>=nums[dq[-1]]:
            dq.pop()
        dq.append(index)
        
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #Soultion 3 much quicker use a pointer to point the max value in window
        if not nums or k == 0: return []
        reuslt = [0] * (len(nums) - k + 1)
        last_max_index = -1
        for i in range(len(nums) - k + 1):
            if last_max_index < i:
                last_max_index = i
                for j in range(i, i + k):
                    if nums[j] > nums[last_max_index]: last_max_index = j
            elif nums[last_max_index] < nums[i + k - 1]: last_max_index = i + k - 1
            reuslt[i] = nums[last_max_index]
        return reuslt
        
        
        #Solution 2 use dequeue
        # if k==1:
        #     return nums
        # if len(nums)==0:
        #     return []
        # dq= deque()
        # for i in range(k):
        #     self.add_to_deq(dq, nums, i)
        # result = []
        # start = 0
        # for i in range(k-1,len(nums)):
        #     self.add_to_deq(dq, nums, i)
        #     while dq[0]<start:
        #         dq.popleft()
        #     result.append(nums[dq[0]])
        #     start+=1
        # return result
               
        
        #Solution 1, use PriorityQueue, find max value in a k-sized Priority Queue
#         if len(nums)==0:
#             return []
#         pq = PriorityQueue()
#         result = []
#         if k==1:
#             return nums
#         start=0
#         for i in range(k):
#             pq.put((-nums[i],i))
        
#         for i in range(k-1,len(nums)):
#             pq.put((-nums[i],i)) 
#             value, index = self.findMax(pq, start)        
#             result.append(-value)   
#             start+=1
#         return result
            
            
        
        
        


import collections
import heapq as h
#Provided three solutions:
#O(n*log n) using heap
#O(n) using deque
#O(n*K) by brute
class Solution:
    def get_current_max(self,heap, start):
        while True:
            m, idx = h.heappop(heap)
            if idx>= start:
                return m*(-1), idx
    def find_max_in_window(self, nums, start,end):
        answer= -2**31
        for i in range(start, end+1):
            answer = max(answer, nums[i])
        return answer

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #Now deque again: 
        window, result = [], []
        for i, x in enumerate(nums):
            if i>=k and window[0]<= i-k:
                window.pop(0)
            while len(window) and nums[window[-1]]<=x:
                window.pop()
                #result.append(x)
            window.append(i)
            if i>=k-1:
                result.append(nums[window[0]])
        return result
            
            
            
            
        
        
        
        #Another brute solution
        # result=[]
        # start, end=0, k-1
        # while  end< len(nums) and len(nums):
        #     result.append(self.find_max_in_window(nums, start, end))
        #     start, end = start+1, end+1
        # return result
            
        
        
        #Use max heap
        # if k==0 or len(nums)==0:
        #     return []
        # heap = []
        # for i in range(k):
        #     h.heappush(heap, (nums[i]*(-1),i))
        # result, start, end = [], 0, k-1
        # while end< len(nums):
        #     m, idx = self.get_current_max(heap, start)
        #     result.append(m)
        #     h.heappush(heap,(m*(-1), idx))
        #     start, end = start+1, end+1
        #     if end< len(nums):
        #         h.heappush(heap,(nums[end]*-1, end))
        # return result
            
        
        
        
        

            
            
        
        
        # if not nums: return []
        # window, res = [], []
        # for i, x in enumerate(nums):
        #     if i>=k and window[0]<= i-k:
        #         window.pop(0)
        #     while window and nums[window[-1]]<= x:
        #         window.pop()
        #     window.append(i)
        #     if i>=k-1:
        #         res.append(nums[window[0]])
        # return res
        
        # if not nums: return []
        # window, res = [],[]
        # for i, x in enumerate(nums):
        #     if i>=k and window[0]<= i-k:
        #         window.pop(0)
        #     while window and nums[window[-1]] <=x:
        #         window.pop()
        #     window.append(i)
        #     if i >= k-1:
        #         res.append(nums[window[0]])
        # return res
        
        #Contains max() operation, so it is slow
        # output=[]
        # window= collections.deque([])
        # count=0
        # if len(nums)<k:
        #     return None
        # for i in range(len(nums)):
        #     if count< k-1:
        #         window.append(nums[i])
        #     else:
        #         window.append(nums[i])
        #         output.append(max(window))
        #         window.popleft()
        #     count +=1
        # return output     
        
        #This solution is quite slow, only beats 4.91%
        # output=[]
        # window= collections.deque([])
        # count=0
        # if len(nums)<k:
        #     return None
        # for i in range(len(nums)):
        #     if count< k-1:
        #         window.append(nums[i])
        #     else:
        #         window.append(nums[i])
        #         output.append(max(window))
        #         window.popleft()
        #     count +=1
        # return output       
        
