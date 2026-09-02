class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        def island_area(i,j):
            if i < 0 or i > n -1 or j < 0 or j > m - 1 or grid[i][j]!= 1:
                return 0 
            grid[i][j] = 0
            
            return 1 + island_area(i + 1, j)+ island_area(i - 1, j)+ island_area(i, j + 1) + island_area(i, j - 1)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = island_area(i,j)
                    max_area = max(max_area,area)
                else:
                    continue
        return max_area