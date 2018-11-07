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
        
