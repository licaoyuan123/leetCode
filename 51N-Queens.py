class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        self.search(n, [], result)
        return result
    
    def search(self, n, cols, result):
        row = len(cols)
        if row==n:
            result.append(self.draw_chessboard(cols))
            return
        for col in range(n):
            if not self.is_valid(cols, row, col):
                continue
            cols.append(col)
            self.search(n, cols, result)
            cols.pop()
            
    def draw_chessboard(self, cols):
        n = len(cols)
        board = []
        for i in range(n):
            row = ['Q' if j==cols[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board
    def is_valid(self, cols, row, col):
        for r, c in enumerate(cols):
            if c==col:
                return False
            if r-c==row-col or r+c==row+col:
                return False
        return True
        
