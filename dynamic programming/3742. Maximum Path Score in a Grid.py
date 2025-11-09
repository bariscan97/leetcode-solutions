class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:

        @lru_cache(None)
        def dp(i, j, cost):
            if cost < 0:
                return -inf
            
            if (i, j) == (m - 1, n  -1):
                return 0
            
            val = -inf
            for r, c in [(i + 1, j),(i, j + 1)]:
                if -1 < r < m and -1 < c < n:
                    match grid[r][c]:
                        case 0: val = max(val, dp(r,c, cost))
                        case 1: val = max(val, dp(r,c, cost - 1) + 1)
                        case 2: val = max(val, dp(r,c, cost - 1) + 2)
            return val

        m = len(grid)
        n = len(grid[0])
        
        res = dp(0,0,k)
        
        return res if res > -inf else -1