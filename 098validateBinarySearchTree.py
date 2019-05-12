# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root, lo=-float('inf'), hi = float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if lo<root.val<hi:
            return self.isValidBST(root.left, lo, min(hi,root.val)) and self.isValidBST(root.right,max(root.val, lo), hi)
       # return 
        
        #My initial solution, however it is out of time limition
#         if root==None:
#             return True
#         if root.left!=None:
#             if self.ma(root.left)>=root.val:
#                 return False
#         if root.right!=None:
#             if root.val>=self.mi(root.right):
#                 return False
        
#         return self.isValidBST(root.left) and self.isValidBST(root.right)
#     def ma(self, root):
#         max_value = root.val
#         if root.left and self.ma(root.left)>max_value:
#             max_value = self.ma(root.left)
#         if root.right and self.ma(root.right)>max_value:
#             max_value = self.ma(root.right)
#         return max_value
            
#     def mi(self, root):
#         min_value = root.val
#         if root.left and self.mi(root.left)<min_value:
#             min_value = self.mi(root.left)
#         if root.right and self.mi(root.right)<min_value:
#             min_value = self.mi(root.right )
#         return min_value



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
        
        
        
