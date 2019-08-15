# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object): 
    s=0
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        ans=0
        stack=[root]
        while stack:
            node=stack.pop()
            if node:
                if L<=node.val<=R:
                    ans+=node.val
                if L<node.val:
                    stack.append(node.left)
                if R>node.val:
                    stack.append(node.right)
        return ans
        
        # def dfs(node):
        #     if node:
        #         if L<=node.val<=R:
        #             self.ans+=node.val
        #         if L<node.val:
        #             dfs(node.left)
        #         if node.val<R:
        #             dfs(node.right)
        # self.ans=0
        # dfs(root)
        # return self.ans
        
        
        # if not root:
        #     return
        # self.rangeSumBST(root.left, L, R)
        # if root.val>=L and root.val<=R:
        #     self.s+=root.val
        # elif root.val>R:
        #     return self.s
        # self.rangeSumBST(root.right, L, R)
        # return self.s        
