# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack=[]
        prev = float("-inf")
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            #result.append(root.val)
            if prev>=root.val:
                return False
            prev = root.val
            root=root.right
        return True
        
        #Third solution
        # if not root:
        #     return True
        # if lo<root.val<hi:
        #     return self.isValidBST(root.left, lo,  min(hi, root.val)) and self.isValidBST(root.right, max(lo, root.val), hi)
        # else:
        #     return False
        
        
        
        #My second solution, inorder traverse the tree
        #to see if it is ancent
        #         if not root:
#             return True
#         stack=[(root, False)]
#         result = []
#         while stack:
#             node, visited=stack.pop()
#             if node and not visited:
#                 stack.append((node.right, False))
#                 stack.append((node, True))
#                 stack.append((node.left, False))
#             if node and visited:
#                 result.append(node.val)
        
#         for i in range(1,len(result)):
#             if result[i]<=result[i-1]:
#                 return False
#         return True
            
            
        
    #My first solution, brute force    
        
#         self.flag=True
#         if not root:
#             return True
        
#         left= self.isValidBST(root.left)
#         right=self.isValidBST(root.right)

#         if root.left and self.dfs(root.left)>=root.val:
#             self.flag=False
#         if root.right and self.dfs_min(root.right)<=root.val:
#             self.flag=False
            
#         return self.flag and left and right
#     def dfs(self, root):
#         #self.max=float("-inf")
#         if not root:
#             return float("-inf")
#         #self.max=max(root.val, self.max)
#         left = self.dfs(root.left)
#         right=self.dfs(root.right)
#         return max(root.val, left, right)
#     def dfs_min(self, root):
#         if not root:
#             return float("inf")
#         left= self.dfs_min(root.left)
#         right=self.dfs_min(root.right)
#         return min(root.val, left, right)
