class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            paths = [
                (i, j + 1),
                (i, j - 1),
                (i + 1, j),
                (i - 1, j)
            ]
            grid[i][j] = 1
            val = False if (i == 0 or i == m - 1 or j == 0 or j == n -1) else True 
            for r, c in paths:
                if -1 < r < m and -1 < c < n and not grid[r][c]:
                    if not dfs(r,c):
                        val = False
            return val

        res = 0
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if not grid[i][j] and dfs(i,j):
                        res += 1
        
        return res