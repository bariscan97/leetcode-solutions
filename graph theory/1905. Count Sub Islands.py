class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs2(i ,j ,color):
            if color != grid1[i][j]:
                return False
            paths = [
                (i + 1, j),
                (i - 1, j),
                (i , j - 1),
                (i , j + 1)
            ]
            visited.add((i,j))
            val = True
            for r, c in paths:
                if -1 < r < m and -1 < c < n and grid2[r][c] == 1 and not (r,c) in visited:
                    if not dfs2(r, c ,color):
                        val = False  
            return val

        def dfs(i ,j ,color):
            grid1[i][j] = color
            paths = [
                (i + 1, j),
                (i - 1, j),
                (i , j - 1),
                (i , j + 1)
            ]
            visited.add((i,j))
            for r, c in paths:
                if -1 < r < m and -1 < c < n and grid1[r][c] == 1 and not (r,c) in visited:
                    dfs(r, c ,color)
        
        visited = set()
        m ,n = len(grid1) , len(grid1[0])
        res = 0
        color = 1
        for i in range(m):
            for j in range(n):
                color += 1
                if grid1[i][j] == 1 and not (i,j) in visited:
                    dfs(i,j,color)
        visited.clear()
        for i in range(m):
            for j in range(n):
                if grid2[i][j] ==  1 and grid1[i][j] > 1 and  not (i,j) in visited:
                    val = dfs2(i,j,grid1[i][j])
                    if val:
                        res += 1
                    
        return res