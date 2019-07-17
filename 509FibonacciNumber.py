class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        
        dp=[0]*(N+2)
        dp[1]=1
        if N<2:
            return dp[N]
        
        for i in range(2, N+1):
            dp[i]+=dp[i-1]
            if i!=1:
                dp[i]+=dp[i-2]
        return dp[N]
