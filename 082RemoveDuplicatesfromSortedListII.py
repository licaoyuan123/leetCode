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
        if not head or not head.next:
            return head
        dummyHead =ListNode(0)
        dummyHead.next=head
        pre= dummyHead
        cur =head
        while cur:
            if cur.next and cur.val==cur.next.val:
                while cur and cur.next and cur.val==cur.next.val:
                    cur=cur.next
                pre.next=cur.next
            else:
                pre=pre.next
            cur=cur.next
            
            
        return dummyHead.next
        
