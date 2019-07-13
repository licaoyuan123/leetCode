class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        M = len(matrix)
        N = len(matrix[0])
        i, j = 0, N-1
        while i<M and j>-1:
            if matrix[i][j]==target:
                return True
            if matrix[i][j]>target:
                j-=1
            if matrix[i][j]<target:
                i+=1
        return False
 
