# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Still not sure about self

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #Here I feel confused about 
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
#         if head==None or head.next ==None:
#             return head
#         curr = head
#         currNext = head.next
        
#         while (curr != None and curr.next != None):
            
#             first= curr
#             second= curr.next
#             first.next = second.next
#             second.next = first
#             curr = curr.next.next
            
#         return currNext
            
        
