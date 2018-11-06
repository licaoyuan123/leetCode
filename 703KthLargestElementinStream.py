#Two solutions 
#First is to use heap O(n)=n * log k
#Second is to use sorted array, O(n)= n* klog(k)
import heapq
class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        # make a heap with reverse order contains k members
        self.heapList= nums
        self.k = k
        heapq.heapify(self.heapList)
        while len(self.heapList)>k:
            heapq.heappop(self.heapList)
    
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heapList)<self.k:
            heapq.heappush(self.heapList, val)
        else:
            heapq.heappushpop(self.heapList, val)

            #         elif val> self.heapList[0]:
#             heapq.heapreplace(self.heapList, val)
        return self.heapList[0]
#     def __init__(self, k, nums):
#         """
#         :type k: int
#         :type nums: List[int]
#         """
#         self.k = k
#         self.nums = sorted(nums)

#     def add(self, val):
#         """
#         :type val: int
#         :rtype: int
#         """
#         bisect.insort_left(self.nums, val)
#         return self.nums[-self.k]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
