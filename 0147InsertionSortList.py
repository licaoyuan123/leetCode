# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummyHead = ListNode(0)
        dummyHead.next=cur=head
        p=dummyHead
        while cur and cur.next:
            if cur.next.val>=cur.val:
                cur=cur.next
                continue
            if cur.next.val<p.next.val:
                p=dummyHead
            while cur.next.val>=p.next.val:
                p=p.next
            p.next,cur.next.next, cur.next  = cur.next,p.next, cur.next.next 
        return dummyHead.next
        
        
