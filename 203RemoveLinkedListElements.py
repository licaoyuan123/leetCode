# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        watch= ListNode(0)
        watch.next = head
        cur = watch
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return watch.next
                
        
        # cur = head
        # if cur.val == val:
        #     return head.next
        # while cur:
        #     if cur.next and cur.next.val ==val:
        #         cur.next = cur.next.next
        #     cur = cur.next
        # return head
        
