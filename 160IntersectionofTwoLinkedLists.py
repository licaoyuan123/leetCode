# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = 0
        lenB = 0
        curA, curB = headA, headB
        while curA!=None:
            lenA+=1
            curA= curA.next
        while curB!=None:
            lenB+=1
            curB =curB.next
        indA, indB = headA, headB
        if lenA>lenB:
            k= lenA-lenB
            for i in range(k):
                indA= indA.next
        else:
            k = lenB-lenA
            for i in range(k):
                indB = indB.next
        while indA!=indB:
            indA= indA.next
            indB = indB.next
        return indA
        
        
        
        # pA, pB = headA, headB
        # while pA!=pB:
        #     if pA:
        #         pA = pA.next
        #     else:
        #         pA = headB
        #     if pB:
        #         pB = pB.next
        #     else:
        #         pB = headA
        #     # pA= (pA==None)? headB:pA.next
        #     # pB = (pB==None)? headA:pB.next
        # return pA
        
        
#         d={}
#         curA = headA
#         index = 0
#         while curA:
#             d[curA] =index
#             index+=1
#             curA = curA.next

#         curB = headB
#         indexB = -1
#         while curB:
#             if curB in d:
#                 indexB= d[curB]
#                 break
#             curB = curB.next
#         if indexB <0:
#             return None
#         res = headB
#         for i in range(indexB):
#             res = res.next
#         return res
            
        
