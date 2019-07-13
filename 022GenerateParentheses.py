class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp=[[] for i in range(n+1)]
        dp[0].append("")
        for i in range(1, n+1):
            #dp[i] = ['('+x+')' for x in dp[i-1] ] 
            for j in range(i):
                dp[i]+= ['('+ x +')'+y for y in dp[j] for x in dp[i-j-1] ] 
        return dp[n]
        #dp[0] = 
        
        
        # left, right = 0,0
        # S = ""
        # ans=[]
        # def dfs(S, left, right, ans):
        #     if len(S)==2*n:
        #         ans.append(S)
        #         return
        #     if left<n:
        #         dfs(S+'(', left+1, right, ans)
        #     if right<left:
        #         dfs(S+")", left, right+1, ans)
        # dfs(S, left, right, ans)
        # return ans
