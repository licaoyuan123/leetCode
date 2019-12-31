class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        matrix=[[1]*(n+1) for _ in range(m+1)]
        for i in range(1, n+1):
            matrix[0][i]=0
        for i in range(1, m+1):
            for j in range(1, n+1):
                matrix[i][j] = matrix[i-1][j] + (s[i-1]==t[j-1])*matrix[i-1][j-1]
        return matrix[-1][-1]
                    
        
        
        
