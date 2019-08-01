# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
#         if not nums:
#             return None
        
        def convert(left, right):
            if left>right:
                return None
            mid= (left+right)//2
            root = TreeNode(nums[mid])
            root.left = convert(left, mid-1)
            root.right = convert(mid+1, right)
            return root
        return convert(0, len(nums)-1)
                
        
        
        # if not nums:
        #     return None
        # mid  =len(nums)//2
        # root = TreeNode(nums[mid])
        # root.left = self.sortedArrayToBST(nums[0:mid])
        # root.right = self.sortedArrayToBST(nums[mid+1:])
        # return root
        
