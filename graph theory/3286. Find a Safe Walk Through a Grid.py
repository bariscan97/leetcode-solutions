class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        
        @cache
        def dfs(i ,j ,last_health):
            
            if last_health < 1:
                return False
            if (i ,j) == (m - 1, n - 1):
                return last_health  >= 1
            paths = [
                (i + 1 ,j),
                (i - 1 ,j),
                (i ,j + 1),
                (i ,j - 1)
            ]
            visited.add((i,j))
            val = False
            for r ,c in  paths:
                if -1 < r < m and -1 < c < n and not (r,c) in visited:
                    val = val or dfs(r, c, last_health - grid[r][c])
            visited.remove((i,j))
            return val
       
        m ,n = len(grid) , len(grid[0])
        visited = set()
        
        return dfs(0 ,0, health - grid[0][0])
        