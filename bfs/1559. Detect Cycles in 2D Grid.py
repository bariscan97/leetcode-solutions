rots = [(1,0),(-1,0),(0,1),(0,-1)]
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
    
        def bfs(x,y,parent):
            q = deque()
            q.append([x,y,parent])
            while q:
                counter = Counter()
                for _ in range(len(q)):
                    r, c ,parent = q.popleft()
                    visited.add((r,c))
                    for i, j in rots:
                        a = r + i
                        b = c + j
                        if -1 < a < m and -1 < b < n and grid[a][b] == parent and not (a, b) in visited:
                            q.append([a, b, parent])
                            if (a,b) in counter:
                                return True
                            counter[(a,b)] += 1
            return False
        
        m, n = len(grid), len(grid[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if not (i,j) in visited:
                    ok = bfs(i,j, grid[i][j])
                    if ok:
                        return True
        return False
