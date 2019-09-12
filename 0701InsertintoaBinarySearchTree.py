#You can not image how elegant the recursive method is!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val>val:
            root.left=self.insertIntoBST(root.left, val)
        else:
            root.right=self.insertIntoBST(root.right, val)
        return root
        
#         if not root:
#             root=TreeNode(val)
#             return root
        
#         dummyNode= TreeNode(0)
#         dummyNode.right=root
        
#         stack=[]
#         #Find the first node that is larger than val, named root
#         while root or stack:
#             while root:
#                 stack.append(root)
#                 root=root.left
            
#             root=stack.pop()
#             if root.val>val:
#                 break
#             prev = root
#             root=root.right
            
#         if not root:
            
#             root=TreeNode(val)
#             prev.right=root
#         else:
#             if not root.left:
#                 root.left=TreeNode(val)
#             else:
#                 temp=root.left
#                 root.left=TreeNode(val)
#                 root=root.left
#                 root.left=temp
#         return dummyNode.right
        
        
        
