# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    memo={1:[TreeNode(0)]}
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N in self.memo:
            return self.memo[N]
        ret=[]
        for l in range(1, N, 2):
            for left in self.allPossibleFBT(l):
                for right in self.allPossibleFBT(N-l-1):
                    root = TreeNode(0)
                    root.left=left
                    root.right=right
                    ret.append(root)
        self.memo[N] = ret
        return self.memo[N]
        
        
        # res = []
        # if not N%2:
        #     return res
        # if N==1:
        #     header = TreeNode(0)
        #     res.append(header)
        #     return res
        # if N==3:
        #     header =TreeNode(0)
        #     header.left=TreeNode(0)
        #     header.right=TreeNode(0)
        #     res.append(header)
        #     return res
        # def construct(n):
            
