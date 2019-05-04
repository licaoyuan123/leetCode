# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#import heapq as hq
#Solution 0, best in theory however it is slower than my own solution 1 below, Time O(n), space O(k)
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq =PriorityQueue()
        for node in lists:
            if node:
                pq.put((node.val, node))
        dummy=ListNode(0)
        cur = dummy
        while not pq.empty():
            cur.next = pq.get()[1]
            cur = cur.next
            if cur.next:
                pq.put((cur.next.val, cur.next))
        return dummy.next
        
        
#My solution, combine all list to an array then sort and constract a new list
#Time: O(nlog n), Space: O(n)
#         result=[]
#         for i in range(len(lists)):
#             while lists[i]:
#                 result.append(lists[i].val)
#                 lists[i]= lists[i].next

#         result.sort()
#         head, node =ListNode(0), ListNode(0)
#         head= node
#         for x in range(len(result)):
# 	        node.next= ListNode(result[x])
# 	        node = node.next
#         final= head.next
#         return final
    
                
        
