# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #Solution 4 use flag
        if not root:
            return []
        stack, path=[(root, False)], []
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    path.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return path
        
        
        #Solution 3 Nonrecursive， reverse preOrder root right, left
        # if not root:
        #     return []
        # stack, path=[root], []
        # while stack:
        #     node=stack.pop()
        #     if node:
        #         path.append(node.val)
        #         stack.append(node.left)
        #         stack.append(node.right)
        # return path[::-1]
        
        #Solution 2 divide and conque
        # if not root:
        #     return []
        # path=[]
        # left = self.postorderTraversal(root.left)
        # right= self.postorderTraversal(root.right)
        # path=left+right+[root.val]
        # return path
        
        
        #Solution 1 recursively
    #     if not root:
    #         return []
    #     path=[]
    #     self.helper(root, path)
    #     return path
    # def helper(self,root, path):
    #     if not root:
    #         return
    #     self.helper(root.left, path)
    #     self.helper(root.right, path)
    #     path.append(root.val)
        

        
