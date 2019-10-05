# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        L=0
        dummyHead = ListNode(0)
        dummyHead.next= head
        cur = dummyHead
        while cur.next:
            L+=1
            cur = cur.next
        L-=n
        cur= dummyHead
        while L:
            L-=1
            cur= cur.next
        cur.next= cur.next.next
        return dummyHead.next
            
        
        
        # dummyHead= ListNode(0)
        # dummyHead.next = head
        # first, second = dummyHead, dummyHead
        # while n:
        #     first =first.next
        #     n-=1
        # # if not first:
        # #     return None
        # while first.next:
        #     first = first.next
        #     second= second.next
        # second.next=second.next.next
        # return dummyHead.next
        
