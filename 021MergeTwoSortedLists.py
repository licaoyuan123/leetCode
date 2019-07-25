# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        dummyHead = ListNode(0)
        cur= dummyHead
        while l1 and l2:
            if l1.val<l2.val:
                cur.next=l1
                l1= l1.next
            else:
                cur.next=l2
                l2 =l2.next
            cur = cur.next
        cur.next= l1 or l2
        return dummyHead.next
        
        
#         dummyHead = ListNode(0)
#         cur = dummyHead
#         while l1 or l2:
#             if l1 and l2:
#                 l1.val
            
            
#             cur.next= ListNode(l1.val if (l1 and l1.val<l2.val) else l2.val )
        
