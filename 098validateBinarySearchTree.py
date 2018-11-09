# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#Easist way is to travel all the values and judge if it is ordered.
class Solution:
    def isValidBST(self, root, min1= None, max1 = None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(not root):
            return True
        if(min1 !=None and root.val<= min1):
            return False
        if(max1 !=None and root.val>= max1):
            return False
        return self.isValidBST(root.left, min1, root.val) and self.isValidBST(root.right, root.val, max1)
        
        
    #     self.prev=None
    #     return self.helper(root)
    # def helper(self, root):
    #     if root is None:
    #         return True
    #     if not self.helper(root.left):
    #         return False
    #     if self.prev and self.prev.val>=root.val:
    #         return False
    #     self.prev=root
    #     return self.helper(root.right)
        
#         if not root:
#             return True
#         all_value = []
#         self.travel(root, all_value)
#         # test= sorted(all_value)
#         # return test==all_value
#         for i in range(len(all_value)-1):
#             if all_value[i]>= all_value[i+1]:
#                 return False
#         return True
        
#     def travel(self,root, all_value):
#         if root is None:
#             return
#         self.travel(root.left, all_value)
#         all_value.append(root.val)
#         self.travel(root.right, all_value)
        
        
        
