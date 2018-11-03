# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head ==None:
            return None
        allNodes ={ListNode(-1)}
        while(head):
            if head in allNodes:
                return head
            allNodes.add(head)
            head = head.next
        return None
#         fast=slow=head
        
#         while head:
#             try:
#                 fast = fast.next.next
#                 slow= slow.next
#                 if fast==slow:
#                     return fast
                
#             except:
#                 return None
                
#         return None
        
