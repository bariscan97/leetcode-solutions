class Solution:
    def knightDialer(self, n: int) -> int:
        
        @cache
        def dfs(i ,j ,cnt):
            
            if cnt == n :
                return 1                
            
            paths = [
                (i + 2 ,j + 1),
                (i + 2 ,j - 1),
                (i - 2 ,j + 1),
                (i - 2, j - 1),
                (i + 1 ,j + 2),
                (i + 1 ,j - 2),
                (i - 1 ,j + 2),
                (i - 1, j - 2)
            ]
            
            val = 0
            
            for r ,c in paths :
                if -1 < r < 4 and -1 < c < 3:
                    if not grid[r][c] and cnt < n:
                        val += dfs(r ,c ,cnt + 1) 
                        
            return val 
        
        grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [1, 0, 1],
        ]
        res = -1
        MOD = 10 ** 9 + 7
        for i in range(4):
            for j in range(3):
                if grid[i][j] == 0: 
                    res += dfs(i ,j, 1)
        return res % MOD + 1