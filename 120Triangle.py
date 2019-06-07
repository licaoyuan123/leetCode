import numpy as np
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle)==0:
            return 0
        if len(triangle)==1:
            return min(triangle[0])
        curPre=triangle[0]
        for i in range(1, len(triangle)):
            cur=[0]*len(triangle[i])
            cur[0] = curPre[0]+ triangle[i][0]
            cur[-1] = curPre[-1]+ triangle[i][-1]
            for j in range(1, len(cur)-1):
                cur[j] =triangle[i][j]+ min(curPre[j], curPre[j-1] )
            curPre = cur
        return min(curPre)
                
        
        
        #My second solution, adjance is ignored
        # for i in range(1, len(triangle)):
        #     cur= [0]*(len(curPre)*len(triangle[i]))
        #     for j in range(0, len(curPre)):
        #         for k in range(0, len(triangle[i])):
        #             cur[j*len(triangle[i]) + k ] = curPre[j]+triangle[i][k]
        #     curPre = cur
        # return min(curPre)
            #cur = np.array()+np.array(triangle[i])

        
        #My first solution is greddy however here need DP
#         if len(triangle)==0:
#             return 0
#         if len(triangle)==1:
#             return min(triangle[0])
        
#         dis = [0]*len(triangle)
#         dis[0] = triangle[0][0]
#         for i in range(1, len(triangle)):
#             dis[i] = min(np.array( [dis[i-1]]*len(triangle[i])) + np.array(triangle[i]) )
#         return dis[-1]
        
