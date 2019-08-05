"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        temp, dic = head, {}
        while temp:
            dic[temp] = Node(temp.val, None, None)
            temp=temp.next
        temp=head
        while temp:
            if temp.next:
                dic[temp].next = dic[temp.next]
            if temp.random:
                dic[temp].random =dic[temp.random]
            temp=temp.next
        return dic[head]
        
#         if not head:
#             return None
#         temp = head
#         while temp:
#             newNode  =Node(temp.val, temp.next, None)
#             temp.next = newNode
#             temp=temp.next.next
#         temp=head
        
#         while temp:
#             if temp.random:
#                 temp.next.random=temp.random.next
#             temp = temp.next.next
        
#         old =head
#         new=head.next
#         new_head = head.next
#         while new.next:
#             old.next= new.next
            
#             new.next= new.next.next
#             old = old.next
#             new = new.next
#         old.next = None
#         new.next = None
#         return new_head
        
        
