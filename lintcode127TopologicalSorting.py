#Need to figure out why this solution do not work
"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from queue import deque
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return []
            
        #First need to find the head of the graph
        head  = []
        headNode = None
        dic_1 = {}
        for node in graph:
            for neighbor in node.neighbors:
                dic_1[neighbor] = 1
        for node in graph:
            if node not in dic_1:
                head.append(node)
                

        dic = {}
        result = []
        dic[headNode] = 1
        dq = deque()
        for node in head:
            dic[node] = 1
            dq.append(node)

        while dq:
            node = dq.popleft()
            result.append(node)
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    dic[neighbor] = 1
                    dq.append(neighbor)
        return result
                
                    
