# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # if not head:
        #     return None
        # if not head.next:
        #     return TreeNode(head.val)
        #print(5/2)
        size = self.findLength(head)
        self.current = head
        
        return self.helper(size)
    
    def findLength(self, head):
        count = 0
        while head:
            count+=1
            head=head.next
        return count
    def helper(self, size):
        if size<=0:
            return None
        left = self.helper(size//2)
        root = TreeNode(self.current.val)
        self.current = self.current.next        
        right = self.helper(size-1-size//2)
        
        root.left = left
        root.right = right
        return root
    
    #     if not head:
    #         return head
    #     if not head.next:
    #         return TreeNode(head.val)
    #     pre_mid, mid= self.findMiddle(head)
    #     pre_mid.next=None
    #     root = TreeNode(mid.val)
    #     root.left = self.sortedListToBST(head)
    #     root.right = self.sortedListToBST(mid.next)
    #     return root
    # def findMiddle(self, head):
    #     slow=fast=pre_mid=head
    #     while fast and fast.next:
    #         pre_mid=slow
    #         slow=slow.next
    #         fast= fast.next.next
    #     return pre_mid, slow
        
