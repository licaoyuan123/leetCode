# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #path=[]
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #solution3 divide and conque
        if not root:
            return []
        result=[]
        result.append(root.val)
        left=self.preorderTraversal(root.left)
        right=self.preorderTraversal(root.right)
        result=result+left+right
        return result

        #solution 1 non recursive
        # if not root:
        #     return []
        # stack, path=[], []
        # stack.append(root)
        # while stack:
        #     node = stack.pop()
        #     path.append(node.val)
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        # return path
        
        
        #Solution 2 recursive
    #     path=[]
    #     self.helper(root, path)
    #     return path
    # def helper(self, root, path):
    #     if not root:
    #         return
    #     path.append(root.val)
    #     self.helper(root.left, path)
    #     self.helper(root.right, path)
        
        
        
