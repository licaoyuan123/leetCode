# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
       
        slow=fast= head
        while fast and fast.next:
            slow=slow.next
            fast = fast.next.next
        pre, cur= None, slow
        while cur:
            pre,  cur.next, cur = cur, pre, cur.next
        second = pre
        first=head
        while second.next:
            first.next, first= second, first.next
            second.next, second =first, second.next
        return dummyHead.next
            
            
