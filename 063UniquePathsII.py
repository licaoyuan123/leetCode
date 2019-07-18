import numpy as np
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """     
        if obstacleGrid[0][0]==1:
            return 0
        
        obstacleGrid[0][0]=1
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(1,m):
            obstacleGrid[i][0]= int( obstacleGrid[i-1][0]==1 and obstacleGrid[i][0]==0 )
        for j in range(1, n):
            obstacleGrid[0][j]= int( obstacleGrid[0][j-1]==1 and obstacleGrid[0][j]==0 )
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    obstacleGrid[i][j]= obstacleGrid[i-1][j] +obstacleGrid[i][j-1]
                    
                else:
                    obstacleGrid[i][j]= 0
        #print(obstacleGrid)
        return obstacleGrid[m-1][n-1]
        
        
        
#         if obstacleGrid[0][0]:
#             return 0
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
#         result = [[0]*n]*m
                
                
        
#         result = 1-np.array(obstacleGrid)
#         ob=-1
#         for i in range(m):
#             if obstacleGrid[i][0]:
#                 ob= i
#                 break
#         if ob>=0:
#             for i in range(ob,m):
#                 result[i][0]=0
#         ob=-1
#         for j in range(n):
#             if obstacleGrid[0][j]:
#                 ob=j
#                 break
#         if ob>=0:
#             for j in range(ob,n):
#                 result[0][j]=0
                
#         for i in range(1,len(obstacleGrid)):
#             for j in range(1, len(obstacleGrid[0])):
#                 if not obstacleGrid[i][j]:
#                     result[i][j]= result[i-1][j]+result[i][j-1]
#         return result[-1][-1]
