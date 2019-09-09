# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Solution 4 BFS
        max_depth=0
        
        level=[root] if root else []
        while level:
            max_depth+=1
            queue=[]
            for node in level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #queue.append()
            level = queue
        return max_depth
        
        
        
        #Solution 3 non recursive
        
#         if not root:
#             return 0
#         max_depth = 0
#         stack=[(root, 1)]
#         while stack:
#             node, depth=stack.pop()
            
#             if node:
#                 max_depth=max(max_depth, depth)
#                 stack.append((node.right, depth+1))
#                 stack.append((node.left, depth+1))
#         return max_depth
        
        
        
        #Solution 2 recursive, divide and conque
        
#         if not root:
#             return 0
        # left= self.maxDepth(root.left)
        # right=self.maxDepth(root.right)
        # return 1+max(left, right)
        
        #Solution 1 recursive, traverse
        # if not root:
        #     return 0
        # return 1+ max( self.maxDepth(root.left), self.maxDepth(root.right))
    
        
        
