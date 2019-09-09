# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.balance=True
        self.getHeight(root)
        return self.balance
    def getHeight(self, root):
        if not root:
            return 0
        left=self.getHeight(root.left)
        right=self.getHeight(root.right)
        if abs(left-right)>1:
            self.balance=False
        return max(left, right)+1
        
        
#         if not root:
#             return True
#         return self.getHeight(root) !=-1

#     def getHeight(self, root):
#         if not root:
#             return 0
#         left = self.getHeight(root.left)
#         right =  self.getHeight(root.right)
#         if abs(left-right)>1 or left==-1 or right==-1:
#             return -1
#         return max(left,right)+1 
        
