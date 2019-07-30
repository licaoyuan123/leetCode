# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        before=before_head=ListNode(0)
        after=after_head =ListNode(0)
        while head:
            if head.val<x:
                before.next=head
                before=before.next
            else:
                after.next=head
                after=after.next
            head=head.next
        after.next=None
        before.next=after_head.next
        return before_head.next
        
        
        
        # if not head or not head.next:
        #     return head
        # dummyHead = ListNode(0)
        # dummyHead.next=head
        # left=right=dummyHead
        # while True:
        #     while left.next:
        #         if left.next.val<=x:
        #             left = left.next
        #     while right.next:
        #         if right.next.val>x:
        #             right = right.next
        #     if left.next and right.next:
        #         right.next, right.next.next, left.next, left.next.next = left.next, left.next.next, right.next, right.next.next
        #         left=left.next
        #         right=right.next
        #     else:
        #         left.next=None
        #         right.next=None
        #         return dummyHead.next
                
        
