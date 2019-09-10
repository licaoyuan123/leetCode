"""
The key is, from https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/39775/Accepted-short-solution-in-Java
1. A path from start to end, goes up on the tree for 0 or more steps, then goes down for 0 or more steps. Once it goes down, it can't go up.
Each path has a highest node, which is also the lowest common ancestor of all other nodes on the path.

2 A recursive method maxPathDown(TreeNode node)
  (1) computes the maximum path sum with highest node is the input node, update maximum if necessary
  (2) returns the maximum sum of the path that can be extended to input node's parent.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = float("-inf")
        self.helper(root)
        return self.max
        
    def helper(self, root):
        if not root:
            return 0
        left= max(0, self.helper(root.left))
        right=max(0, self.helper(root.right))
        self.max = max(self.max, root.val+left+right)
        return max(left, right)+root.val
        
