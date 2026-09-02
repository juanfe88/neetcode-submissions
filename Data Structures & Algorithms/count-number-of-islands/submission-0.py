class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        islands = 0
        def explore(i,j):
            if i < 0 or i > n -1 or j < 0 or j > m - 1 or grid[i][j]!= "1":
                return
            grid[i][j] = "0"
            explore(i+1,j)
            explore(i-1,j) 
            explore(i,j+1) 
            explore(i,j-1)
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    islands+=1
                    explore(i,j)
                else:
                    continue
        return islands

