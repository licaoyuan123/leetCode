"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from queue import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #DFS recursive
        if not node:
            return
        new_node = Node(node.val, [])
        dic = {}
        dic[node] = new_node
        stack = [node]
        self.dfs(stack, dic)
        return new_node
    def dfs(self, stack, dic):
        if not stack:
            return
        node = stack.pop()
        for neighbor in node.neighbors:
            if neighbor not in dic:
                new_neighbor = Node(neighbor.val, [])
                dic[neighbor] = new_neighbor
                stack.append(neighbor)
                self.dfs(stack, dic)
            dic[node].neighbors.append(dic[neighbor])
        
        
        #DFS iteratively:
        # if not node:
        #     return None
        # dic={}
        # new_node = Node(node.val, [])
        # dic[node] = new_node
        # stack=[node]
        # while stack:
        #     node = stack.pop()
        #     for neighbor in node.neighbors:
        #         if neighbor not in dic:
        #             new_neighbor = Node(neighbor.val, [])
        #             dic[neighbor] = new_neighbor
        #             stack.append(neighbor)
        #         dic[node].neighbors.append(dic[neighbor])
        # return new_node

        
        
        
        
        
        
        
        
        
        
        #BFS
        # if not node:
        #     return None
        # new_node = Node(node.val, [])
        # dq = deque([node])
        # dic={}
        # dic[node] = new_node
        # while dq:
        #     node = dq.popleft()
        #     for neighbor in node.neighbors:
        #         if neighbor not in dic:
        #             new_neighbor = Node(neighbor.val, [])
        #             dic[neighbor] = new_neighbor
        #             dq.append(neighbor)
        #         dic[node].neighbors.append(dic[neighbor])
        # return new_node
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if not node:
        #     return None
        # new_node = Node(node.val, [])
        # dic = {node:new_node}
        # dq = deque([node])
        # while dq:
        #     next_node = dq.popleft()
        #     for neighbor in next_node.neighbors:
        #         if neighbor not in dic:
        #             neighbor_copy = Node(neighbor.val, [])
        #             dic[neighbor] = neighbor_copy
        #             dq.append(neighbor)
        #         dic[next_node].neighbors.append(dic[neighbor])
        # return new_node

            
        

        
        #Wrong attempt
        #         #BFS?
#         if not node:
#             return None
#         dq = deque()
#         dq.append(node)
#         dic={}
#         #Clone the nodes
#         while dq:
#             next_node = dq.popleft()
#             newNode = Node(next_node.val, [])
#             #neigh_list = []
#             dic[next_node] = newNode
#             for n in next_node.neighbors:
#                 if not n in dic:
#                     dq.append(n)
#                 # new_neib = Node(n.val, [])
#                 # newNode.neighbors.append(new_neib)
#             #dq.popleft()
#         #Connect the nodes
        
#         dq.append(node)
#         dic_new = {}
#         #dic_new[node]=1
#         while dq:
#             next_node = dq.popleft()
#             dic_new[next_node] =1
#             for nei in next_node.neighbors:
#                 if nei not in dic_new:
#                     dic[next_node].neighbors.append(dic[nei])
#                     dq.append(nei)
#         return dic[node]
            
            
        
        
        
