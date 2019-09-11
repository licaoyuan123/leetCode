# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return None
        stack, result=[], []
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            k-=1
            if not k:
                break
            #result.append(root.val)
            root=root.right
        return root.val
        
