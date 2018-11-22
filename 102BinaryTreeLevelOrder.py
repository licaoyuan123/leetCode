# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # ans, level=[], [root]
        # while root and level:
        #     ans.append([node.val for node in level])
        #     LRpair  = [(node.left, node.right) for node in level]
        #     level = [leaf for LR in LRpair for leaf in LR if leaf]
        # return ans
        
        # ans, level=[],[root]
        # while root and level:
        #     ans.append([node.val for node in level])
        #     level =[kid for n in level for kid in (n.left, n.right) if kid]
        # return ans
        ans, level = [],[root]
        while root and level:
            sub_ans=[]
            for node in level:
                sub_ans.append(node.val)
            ans.append(sub_ans)
            sub_level=[]
            for node in level:
                if node.left:
                    sub_level.append(node.left)
                if node.right:
                    sub_level.append(node.right)
            level = sub_level
        return ans


            
