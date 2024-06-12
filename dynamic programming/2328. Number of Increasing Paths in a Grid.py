class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
       
        @cache
        def dfs(i,j):
            val = 1
            paths = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            visited.add((i,j))
            for r, c in paths:
                if 0 <= r < m and 0 <= c < n and not (r,c) in visited:
                    if grid[r][c] > grid[i][j]:
                        val += dfs(r,c)
            visited.remove((i,j))
            return val

        m = len(grid)
        n = len(grid[0])
        MOD = 10 ** 9 + 7
        visited = set()
        ans = 0
        for i in range(m):
            for j in range(n):
                res = dfs(i,j)
                ans += res
                ans %= MOD
        return ans
        
        