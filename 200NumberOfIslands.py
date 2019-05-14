class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    self.dfs(i, j, grid)
                    count +=1
        return count
    
    def dfs(self, i, j, grid):
        if i<0 or i> len(grid)-1 or j<0 or j>len(grid[0])-1 or grid[i][j]!="1":
            return
        grid[i][j]="#"
        self.dfs(i-1, j, grid)
        self.dfs(i+1, j, grid)
        self.dfs(i, j-1, grid)
        self.dfs(i, j+1, grid)
        

#         if not grid:
#             return 0
        
#         def sink(i,j):
#             count = 0
#             if i<0 or i>len(grid)-1 or j<0 or j>len(grid[0])-1 or grid[i][j]!="1":
#                 return 0
#             grid[i][j]="0"
#             map(sink,[i-1, i+1, i, i], [j, j, j-1, j+1] )
#             return 1
#         return sum(sink(i,j) for i in range(0,len(grid)) for j in range(0,len(grid[0])))
