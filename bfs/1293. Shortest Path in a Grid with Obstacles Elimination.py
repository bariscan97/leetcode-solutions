class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        d = [(0,1), (1,0), (-1,0), (0,-1)]
        m = len(grid)
        n = len(grid[0])
        if k >= m + n - 2:
            return m + n - 2
        q = deque([(0,0,k)])
        visited = {(0,0): 0}
        step = 0
        while q:
            for _ in range(len(q)):
                r, c, left = q.popleft()
                if r == m - 1 and c == n - 1:
                    return step
                for dr, dc in d:
                    nexR = dr + r
                    nexC = dc + c
                    if 0 <= nexR < m and 0 <= nexC < n:
                        if left == 0 and grid[nexR][nexC] == 1:
                            continue
                        if (nexR, nexC) not in visited or visited[(nexR, nexC)] < left:
                            visited[(nexR, nexC)] = left
                            q.append((nexR, nexC, left - grid[nexR][nexC]))
            step += 1

        
        return -1