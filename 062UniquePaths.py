import numpy as np
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result = [[1 for i in range(n)] for j in range (m)]
        
        for i in range(1,m):
            for j in range(1,n):
                result[i][j] = result[i][j-1]+result[i-1][j]
        return result[-1][-1]
#         if m==1 or n==1:
#             return 1
        
#         result=np.array([[0]*n]*m)
#         result[0,:]= np.array([1]*n)
#         result[:,0] = np.array([1]*m)
#         for i in range(1,m):
#             for j in range(1, n):
#                 result[i, j] = result[i-1,j]+result[i, j-1]
#         #print(result)
#         return result[m-1, n-1]
        
