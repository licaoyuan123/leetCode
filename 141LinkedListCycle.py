# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # try:
        #     slow = head
        #     fast = head.next
        #     while slow is not fast:
        #         slow = slow.next
        #         fast = fast.next.next
        #     return True
        # except:
        #     return False
        
        allNode= {head}
        while(head and head.next):
            if head.next in allNode:
                return True
            allNode.add(head.next)
            head = head.next
            
        return False
        
        
        
        #fast and slow solution
        # if head==None or head.next==None or head.next.next==None:
        #     return False
        # fast = head
        # slow = head
        # while slow.next and fast.next and fast.next.next:
        #     fast=fast.next.next
        #     slow=slow.next
        #     if fast==slow:
        #         return True
        # return False
