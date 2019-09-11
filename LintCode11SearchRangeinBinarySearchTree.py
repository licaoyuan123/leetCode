"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        # if not root:
        #     return []
        result=[]
        stack=[]
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            
            root=stack.pop()
            if root.val>=k1 and root.val<=k2:
                result.append(root.val)
            if root.val>k2:
                break
            root=root.right
        return result
