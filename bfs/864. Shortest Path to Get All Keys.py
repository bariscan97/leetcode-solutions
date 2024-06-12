class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        all_keys = set()
        m ,n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    start = (i,j)
                if not grid[i][j] in ["@","#","."] and grid[i][j].lower() == grid[i][j]:
                    all_keys.add(grid[i][j])
        upper_all_keys = set([i.upper() for i in all_keys])
        res = inf
        que = deque()
        que.append((0 , start[0], start[1] ,[] ))
        while que:
            
            q = deque()
            q.append(que.popleft())
            visited = set()
            
            while q:
                cnt ,r ,c , my_keys  = q.popleft()
                if -1 < r < m and -1 < c < n and grid[r][c] in all_keys and not grid[r][c] in my_keys:
                    if len(my_keys) + 1 == len(all_keys):
                        res = min(res ,cnt)
                    else:
                        que.append((cnt,r,c,my_keys +[grid[r][c]]))
                    continue
                visited.add((r,c))
                paths =  [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
                for x ,y in paths:
                    if -1 < x < m and -1 < y < n and not (x,y) in visited:
                        if grid[x][y] != "#":
                            if (grid[x][y] in upper_all_keys and grid[x][y].lower() in my_keys) or grid[x][y] == "." or grid[x][y] == "@" or grid[x][y] in all_keys :
                                visited.add((x,y))
                                q.append((cnt + 1,x,y,my_keys))
            
            
        return res if res < inf else -1
    
            
        
  
            

        
       