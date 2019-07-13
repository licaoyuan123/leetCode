class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row, column = len(matrix), len(matrix[0])
        total = row*column
        left=0
        right= total-1
        while left<=right:
            mid=(right + left)/2
            if matrix[mid/column][mid%column]==target:
                return True
            if matrix[mid/column][mid%column]< target:
                left=mid+1
            else:
                right=mid-1
        return False
        
        
#        O(M+N), should be solved in O(log(M+N))
#         if not matrix:
#             return False
#         M, N = len(matrix), len(matrix[0])
        
#         row= 0
#         column = N-1
#         while row<M and column>-1:
#             if matrix[row][column]==target:
#                 return True
#             if matrix[row][column]<target:
#                 row+=1
#             else:
#                 column-=1
#         return False
        
