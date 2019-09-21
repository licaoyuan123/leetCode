#After practice, I got similar or better idea than the previous one

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if not head or not head.next or k==1:
            return head
        jump=dummy_node=ListNode(0)
        dummy_node.next=head
        while True:
            start=end=jump.next
            if not end:
                return dummy_node.next

            for _ in range(k-1):
                end=end.next
                if not end:
                    return dummy_node.next
            #reverse start to end
            pre = end.next
            cur=start
            for i in range(k):
                cur.next, cur, pre= pre, cur.next, cur
            jump.next= pre
            jump=start



#Solution from https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11491/Succinct-iterative-Python-O(n)-time-O(1)-space
#How can this guy so smart

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        prehead= jump= ListNode(-1)
        prehead.next= l= r = head
        while True:
            count=0
            while r and count<k:
                r= r.next
                count+=1
            if count==k:
                pre, curr= r, l
                for _ in range(k):
                    curr.next, curr, pre = pre, curr.next, curr
                jump.next, jump, l= pre, l, r  
            else:
                return prehead.next
            
