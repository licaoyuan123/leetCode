# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = float("inf")
    pre= -float("inf")
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        
        self.minDiffInBST(root.left)
        self.res = min(self.res, root.val-self.pre)
        self.pre=root.val
        self.minDiffInBST(root.right)
        return self.res
        
        
