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
        if not head:
            return head
        if not head.next:
            return TreeNode(head.val)
        pre_mid, mid= self.findMiddle(head)
        pre_mid.next=None
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
    def findMiddle(self, head):
        slow=fast=pre_mid=head
        while fast and fast.next:
            pre_mid=slow
            slow=slow.next
            fast= fast.next.next
        return pre_mid, slow
        



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow, fast=head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow=slow.next
        if not slow.next:
            return None
        else:
            root = TreeNode(slow.next.val)
        
        
        root.right = self.sortedListToBST(slow.next.next)
        slow.next=None
        root.left = self.sortedListToBST(head)
        return root
        
