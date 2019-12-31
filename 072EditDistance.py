class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        matrix = [[0]*(n+1) for i in range(m+1)]
        matrix[0]=list(range(n+1))
        
        for i in range(m+1):
            matrix[i][0] = i
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1]==word2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = 1+min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1])

        return matrix[-1][-1]
        
