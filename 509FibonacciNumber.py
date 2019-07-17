class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        a=0
        b=1
        for _ in range(N):
            a, b= b, a+b
        return a
        # count = 0
        # while count<=N:
        #     c=a+b
        #     a=b
        #     b=c
        #     count+=1
        # return c
        
#         dp=[0]*(N+2)
#         dp[1]=1
#         if N<2:
#             return dp[N]
        
#         for i in range(2, N+1):
#             dp[i]+=dp[i-1]
#             if i!=1:
#                 dp[i]+=dp[i-2]
#         return dp[N]
