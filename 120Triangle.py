class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp=triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j]=triangle[i][j]+min(dp[j], dp[j+1])
        return dp[0]
        
        #modify triangle down-top:
        # for i in range(len(triangle)-2, -1, -1):
        #     for j in range(len(triangle[i])):
        #         triangle[i][j]+=min(triangle[i+1][j], triangle[i+1][j+1])
        # #print(triangle)
        # return triangle[0][0]
        
        #Modify triangle, top-down
        # for i in range(1,len(triangle)):
        #     for j in range(len(triangle[i])):
        #         if j==0:
        #             triangle[i][j]+=triangle[i-1][j]
        #         elif j==len(triangle[i])-1:
        #             triangle[i][j]+=triangle[i-1][-1]
        #         else:
        #             if i>1:
        #                 triangle[i][j]+=min(triangle[i-1][j-1], triangle[i-1][j])
        # print(triangle)
        # return min(triangle[-1])
        
        # dp=[[element for element in t] for t in triangle]
        # #print(dp)
        # start=0
        # end=0
        # for i in range(len(triangle)):
        #     start+=triangle[i][0]
        #     end+=triangle[i][-1]
        #     dp[i][0]=start
        #     dp[i][i]= end
        # for i in range(1, len(triangle)):
        #     for j in range(1, len(triangle[i])-1):
        #         dp[i][j] +=min(dp[i-1][j], dp[i-1][j-1])
        # print(dp)
        # return min(dp[-1])
