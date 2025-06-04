class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        @cache
        def dp(i,j):
            if (i, j) == (m - 1, n - 1):
                return grid[i][j]
            
            if  i == m or j == n:
                return inf
            
            return grid[i][j] + min(dp(i + 1, j), dp(i, j + 1))

        m, n = len(grid), len(grid[0])

        return dp(0,0)