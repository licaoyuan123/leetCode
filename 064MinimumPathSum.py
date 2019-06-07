class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dp = [[0]*len(grid[0])] * len(grid)
        # dp[0] = grid[0]
        # dp[:,0] = grid[:,0]
        dp = grid
        for i in range(1, len(grid[0])):
            dp[0][i] = dp[0][i-1]+ dp[0][i]
        
        for j in range(1, len(grid)):
            dp[j][0] += dp[j-1][0]
        
        for i in range(1,len(grid)):
            for j in range(1, len(grid[0])):
                
                dp[i][j] = min(dp[i-1][j] ,dp[i][j-1] ) + grid[i][j] 
        return dp[-1][-1]
        
