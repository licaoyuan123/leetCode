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
            
