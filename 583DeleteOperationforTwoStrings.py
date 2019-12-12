#Similar with the longest common subsquence
class Solution:
    def minDistance(self, str1: str, str2: str) -> int:
        n1=len(str1)
        n2=len(str2)
        if n1==0:
            return n2
        if n2==0:
            return n1
        matrix = [[0 for i in range(n2+1)] for j in range(n1+1)]
        for i in range(n2+1):
            matrix[0][i]=i
        for j in range(n1+1):
            matrix[j][0] = j
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if str1[i-1]==str2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]+1)+1
                    #matrix[i][j] = matrix[i-1][j-1]+2
        return matrix[-1][-1]
