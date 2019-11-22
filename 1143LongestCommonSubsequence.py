#Add the following function to trace the longest subsequence according the table
function backtrack(C[0..m,0..n], X[1..m], Y[1..n], i, j)
    if i = 0 or j = 0
        return ""
    if  X[i] = Y[j]
        return backtrack(C, X, Y, i-1, j-1) + X[i]
    if C[i,j-1] > C[i-1,j]
        return backtrack(C, X, Y, i, j-1)
    return backtrack(C, X, Y, i-1, j)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
    
    #Save O(m)
    class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0]*(len(text2)+1) for _ in range(2)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[1-i%2][j]=dp[i%2][j-1]+1
                else:
                    dp[1-i%2][j] = max(dp[i%2][j], dp[1-i%2][j-1])
        return dp[1-len(text1)%2][-1]

        
        
