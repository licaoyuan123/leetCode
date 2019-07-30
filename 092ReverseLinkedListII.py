# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummyHead = ListNode(0)
        dummyHead.next= head
        leftPre=right=dummyHead
        #left = dummyHead
        for count in range(m-1):
            leftPre=leftPre.next
        for count in range(n):
            right=right.next
        pre = right.next
        left = leftPre.next
        cur=left
        for _ in range(n-m+1):
            cur.next, pre, cur = pre, cur, cur.next
        leftPre.next = pre
        return dummyHead.next
