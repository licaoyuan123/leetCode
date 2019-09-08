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
        if not root:
            return []
        stack, path=[(root, False)], []
        while stack:
            node, visited=stack.pop()
            if node:
                if visited:
                    path.append(node.val)
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return path
        
        
#         if not root:
#             return []
#         path, stack = [], []
#         while True:
#             while root:
#                 stack.append(root)
#                 root=root.left
            
#             if not stack:
#                 return path
#             node=stack.pop()
#             path.append(node.val)
#             root=node.right
        
        
        
        
        
        # if not root:
        #     return []
        # dummyNode=TreeNode(0)
        # dummyNode.right=root
        # stack, path=[],[]
        # stack.append(dummyNode)
        # while stack:
        #     node=stack.pop()
        #     node=node.right
        #     while node:
        #         stack.append(node)
        #         node=node.left
        #     if stack:
        #         path.append(stack[-1].val)
        # return path     
        
        
        #Solution3 non recursive or iterative
#         if not root:
#             return []
#         stack, path=[], []
#         while True:
#             while root:
#                 stack.append(root)
#                 root=root.left
#             if not stack:
#                 return path
#             node=stack.pop()
#             path.append(node.val)
#             root=node.right
        
    
            
        
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
        
