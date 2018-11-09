# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack=[root]
        parent={root:None}
        while p not in parent or q not in parent:
            node= stack.pop()
            if node.left:
                parent[node.left]=node
                stack.append(node.left)
            if node.right:
                parent[node.right]=node
                stack.append(node.right)
        path=set()
        while p:
            path.add(p)
            p=parent[p]
        while q not in path:
            q=parent[q]
        return q
        # while q:
        #     if q in path:
        #         return q
        #     q=parent[q]
            
        
        
        
        
        # if root is None or root==p or root==q:
        #     return root
        # left= self.lowestCommonAncestor(root.left, p,q)
        # right = self.lowestCommonAncestor(root.right, p,q)
        # if left==None:
        #     return right
        # if right==None:
        #     return left
        # return root2
