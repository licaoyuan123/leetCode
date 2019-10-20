from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapify(heap)
        while len(heap)>0:
            if len(heap)==1:
                return -heap[0]
            first = -heappop(heap)
            second = -heappop(heap)
            if second<first:
                heappush(heap, second-first)
        return 0
     
     
     
from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapify(heap)
        while len(heap)>1:
            # if len(heap)==1:
            #     return -heap[0]
            first = -heappop(heap)
            second = -heappop(heap)
            #if second<first:
            heappush(heap, second-first)
        return -heap[-1]
