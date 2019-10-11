# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        stack = [TreeNode(nums[0])]
        #last = None
        for num in nums[1:]:
            node =TreeNode(num)
            if num<stack[-1].val:
                stack[-1].right = node
            else:
                while stack and stack[-1].val<num:
                    node.left = stack.pop()
                if stack:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]
            
            
            
        #     while stack and stack[-1].val<num:
        #         last = stack.pop()
        #     node =TreeNode(num)
        #     if stack:
        #         stack[-1].right = node
        #     if last:
        #         node.left = last
        #     stack.append(node)
        #     last = None
        # return stack[0]
                
