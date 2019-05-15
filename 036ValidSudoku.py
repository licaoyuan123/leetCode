class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            if not self.validate(row):
                return False
        for column in zip(*board):
            if not self.validate(column):
                return False
        for i in (0,3,6):
            for j in (0,3,6):
                square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.validate(square):
                    return False
        return True
    def validate(self, row):
        unit= [i for i in row if i!="."]
        return len(unit)==len(set(unit))
    
    # def validate(self, row):
    #     l = []
    #     for i in range(len(row)):
    #         if row[i]!=".":
    #             l.append(row[i])
    #     n1=len(l)
    #     s = set(l)
    #     if n1!=len(s):
    #         return False
    #     return True
        
