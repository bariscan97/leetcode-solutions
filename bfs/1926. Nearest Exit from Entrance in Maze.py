class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        q = deque()
        q.append([0,*entrance])
        m , n = len(maze), len(maze[0])
        visited = set()
        visited.add(tuple(entrance))
        while q:
            cnt ,i  ,j = q.popleft()
            if (i == m - 1 or i == 0) and cnt > 0:
                return cnt
            if (j == n - 1 or j == 0) and cnt > 0:
                return cnt
            paths = [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]
            for r, c in paths:
                if  -1 < r < m and -1 < c < n and not (r,c) in visited and maze[r][c] == ".":
                    q.append((cnt + 1, r , c))
                    visited.add((r,c))
        return -1
            