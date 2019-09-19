# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return head
        fast=slow=head
        tail = None
        while fast and fast.next :
            tail=slow
            fast=fast.next.next
            slow=slow.next
        tail.next=None
        

        second=self.reverse(slow)
        
        dummy_node=cur = ListNode(0)
        dummy_node.next=head
        first=head
        current=first
        self.combine(head, second)
        return head
    def reverse(self, head):
        cur=head
        pre=None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre
    
    def combine(self, first, second):
        while first:
            n1=first.next
            n2=second.next
            first.next = second
            if not n1:
                break
            first=n1
            second.next=first
            second=n2
        
        
        


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
            
            
