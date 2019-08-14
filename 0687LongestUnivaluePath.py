# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.ans=0
        val = root.val
        def depth(p, parent_val):
            if not p:
                return 0
            left, right = depth(p.left, p.val), depth(p.right, p.val)
            self.ans = max(self.ans, left+right)
            if p.val==parent_val:
                return max(left, right)+1
            else:
                return 0
        
        depth(root, None)
        return self.ans
       
                
        
