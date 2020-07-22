class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        edges=len(connections)
        if edges<n-1:
            return -1
        points=[set() for i in range(n)]
        
        for i,j in connections:
            points[i].add(j)
            points[j].add(i)
        visited=[0]*n
        def dfs(ind):
            #for point in points[ind]:
            if visited[ind]:
                return 0
            visited[ind]=1
            for i in points[ind]:
                dfs(i)
            return 1
        
        connected= sum([dfs(i) for i in range(n)])
        return connected-1
        
        
        # dic={}
        # for conn in connections:
        #     point1=conn[0]
        #     point2=conn[1]
        #     if point1 not in dic:
        #         dic[point1]=1
        #     if point2 not in dic:
        #         dic[point2]=1
        # distinct_point= len(dic.items())
        # #if distinct_point>
        # return n-distinct_point
        
