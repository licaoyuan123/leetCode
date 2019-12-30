class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        # write your code here
        m=len(A)
        n=len(B)
        
        matrix =[ [0]*(m+1) for i in range(n+1) ]
        maxi = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if B[i-1]==A[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]+1
                else:
                    matrix[i][j] = 0
                maxi = max(maxi, matrix[i][j])
        return maxi
        
        
        
        # m=len(A)
        # n=len(B)
        
        # matrix =[ [0]*(m+1) for i in range(n+1) ]
        # for i in range(1, n+1):
        #     for j in range(1, m+1):
        #         if B[i-1]==A[j-1]:
                    
        #             if i>1 and j>1 and B[i-2]==A[j-2]:
        #                 matrix[i][j] = matrix[i-1][j-1]+1
        #             else:
        #                 matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
        #         else:
        #             matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
        # return matrix[-1][-1]
        
