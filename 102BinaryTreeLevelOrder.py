# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level=[root]
        current=[]
        for node in level:
            current.append(node.val)
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
            
        

        
    #         queue= deque([root])
#         result=[]
#         while queue:
#             current_level = []
#             for _ in range(len(queue)):
#                 node=queue.popleft()
#                 current_level.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             result.append(current_level)
        
#         return result
            
        
        
        
        # if not root:
        #     return []
        # queue = [root]
        # result=[]
        # while queue:
        #     current_level=[]
        #     second_queue=[]
        #     for node in queue:
        #         current_level.append(node.val)
        #         if node.left:
        #             second_queue.append(node.left)
        #         if node.right:
        #             second_queue.append(node.right)
        #     result.append(current_level)
        #     queue=second_queue
        # return result
        
