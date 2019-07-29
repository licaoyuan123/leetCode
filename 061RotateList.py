# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        count =0
        cur =head
        while cur:
            cur = cur.next
            count+=1
        rotateTime = k%count
        if k==0 or rotateTime==0:
            return head
        fast=slow=head
        while rotateTime:
            fast = fast.next
            rotateTime-=1
        while fast.next:
            fast=fast.next
            slow=slow.next
        temp=slow.next
        slow.next=None
        fast.next=head
        return temp
        

#         dummyHead = ListNode(0)
#         dummyHead.next = head
#         count=0
#         while count<rotateTime:
#             count+=1
#             cur = dummyHead.next
#             while cur.next.next:
#                 cur = cur.next
#             dummyHead.next, cur.next.next, cur.next= cur.next, dummyHead.next, None
            
#         return dummyHead.next
            
            
        
