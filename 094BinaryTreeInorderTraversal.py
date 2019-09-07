# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #Solution3 non recursive or iterative
        if not root:
            return []
        stack, path=[], []
        while True:
            while root:
                stack.append(root)
                root=root.left
            if not stack:
                return path
            node=stack.pop()
            path.append(node.val)
            root=node.right
        
    
            
        
        #Solution 2 divide and conque
        # path=[]
        # if not root:
        #     return path
        # left = self.inorderTraversal(root.left)
        # right = self.inorderTraversal(root.right)
        # return left+[root.val]+right
        
        
        #Solution 1 recursive traverse
    #     path=[]
    #     self.helper(root, path)
    #     return path
    # def helper(self, root, path):
    #     if not root:
    #         return
    #     self.helper(root.left, path)
    #     path.append(root.val)
    #     self.helper(root.right, path)
        
