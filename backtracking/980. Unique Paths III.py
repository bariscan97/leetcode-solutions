class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
            
        def dfs(i,j,cnt):
            nonlocal res,x
            if grid[i][j] == 2 and cnt == x:
                
                res += 1
                
            paths = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            visited.add((i,j))
            
            for r,c in paths:
                if -1 < r < m and -1 < c < n and not (r,c) in visited and grid[r][c] != -1:
                    if grid[i][j] == 0:
                        dfs(r,c,cnt+1)
                    else:
                        dfs(r,c,cnt)
            visited.remove((i,j))
        visited = set()
        res = 0
        m = len(grid)
        n = len(grid[0])
        x = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i,j)
                if grid[i][j] == 0:
                    x += 1
        dfs(*start,0)
     
        return res