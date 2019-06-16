# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            while cur.next and cur.next.val==cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
        
#         if head==None:
#             return None
#         cur = head
        
#         while cur.next!=None:
#             if cur.next.val == cur.val:
#                 if cur.next.next==None:
#                     cur.next = None
#                 else:
#                     cur.next = cur.next.next
            
#             else:
#                 cur = cur.next
#         return head
