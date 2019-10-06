# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        #inorder left tree, inorder right tree
        first = []
        second = []
        self.preOrder(root1, first)
        self.preOrder(root2, second)
        left=0
        right = len(second)-1
        while left<len(first) and right>-1:
            s=first[left]+second[right]
            if s==target:
                return True
            elif s<target:
                left+=1
            else:
                right-=1
        return False
        
    def preOrder(self, root, nums):
        stack =[]
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            node =stack.pop()
            nums.append(node.val)
            root=node.right
        
