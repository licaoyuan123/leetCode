# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        cur =dummyHead
        x, y, s, curry= 0,0,0,0
        while l1 or l2:
            if l1:
                x= l1.val
                l1 = l1.next
            else:
                x=0
            if l2:
                y=l2.val
                l2 = l2.next
            else:
                y=0
            s = x+y+curry
            curry = s/10
            cur.next = ListNode(s%10)
            cur = cur.next
            
            
        if curry:
            cur.next = ListNode(curry)
            cur = cur.next
        return dummyHead.next
        
        
        
        
        
        
        
        
        #Two solutions come to my mind, first is to convert tbe two 
        #numbers to ineger then add and return a list
        #Second is to add one by one to the end
#         head = ListNode(0)
#         cur = head
#         pre=0
#         while l1 and l2:
#             s= l1.val+l2.val+pre
#             if s>9:
#                 pre=1
#                 s = s%10
#             else:
#                 pre=0
#             cur.val= s
#             cur.next= ListNode(0)
#             cur = cur.next
#             l1 = l1.next
#             l2 = l2.next
#         while l1:
#             cur.val = l1.val+pre
#             cur.next= ListNode(0)
#             cur = cur.next
#             l1=l1.next
#             pre=0
        
            
#             if pre==1:
#                 pre=0
                
            
#         while l2:
#             cur.val = l2.val+pre
#             pre=0
#             cur.next= ListNode(0)
#             cur = cur.next
#             l2 = l2.next
            
#         if pre==1:
#             cur.val = 1
#             pre=0
#             cur = cur.next
            
#         cur1 = head
        
#         while cur1:
#             cur1 = cur1.next
        
#         return head
        
