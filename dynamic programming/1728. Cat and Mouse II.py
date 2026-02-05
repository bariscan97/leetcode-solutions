class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m = len(grid)
        n = len(grid[0])

        def f(jump, r, c):
            yield(r,c)
            for ii in range(1, jump + 1):
                if m > r + ii > -1 and -1 < c < n: 
                    if grid[r + ii][c] == '#':
                        break
                    yield (r + ii, c)
            
            for ii in range(1, jump + 1):
                if m > r - ii > -1 and -1 < c < n : 
                    if grid[r - ii][c] == '#':
                        break
                    yield (r - ii, c)

            for ii in range(1, jump + 1):
                if m > r > -1 and -1 < c + ii < n:
                    if grid[r][c + ii] == '#':
                        break
                    yield (r, c + ii)
            
            for ii in range(1, jump + 1):
                if m > r > -1 and -1 < c - ii < n:
                    if grid[r][c - ii] == '#':
                        break
                    yield (r, c - ii)

            

        @cache
        def dp(turn, mi, mj, ci, cj):
            if (mi, mj) == (ci, cj):
                return False
            
            if turn == m*n*2:
                return False

            if grid[ci][cj] == 'F':
                return False

            if grid[mi][mj] == 'F':
                return True

            if turn % 2:
                for r,c in f(catJump ,ci, cj):
                    if not dp(turn + 1, mi, mj, r, c):
                        return False
                return True

            else:
                for r,c in f(mouseJump ,mi, mj):
                    if dp(turn + 1, r, c, ci, cj):
                        return True
                return False

        cat =  mouse = None             
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'C':
                    cat = (i,j)
                if grid[i][j] == 'M':
                    mouse = (i, j)

        return dp(0,mouse[0],mouse[1],cat[0],cat[1])