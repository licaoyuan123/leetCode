# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result=[]
        queue=deque([root])
        flag=1
        while queue:
            current_level=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if flag%2:
                result.append(current_level)
            else:
                result.append(list(reversed(current_level)))
                
            flag+=1
        return result
        
