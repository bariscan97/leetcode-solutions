class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh_cnt = 0
        res = 0
        for i in range(m):
            for j in range(n):
                match grid[i][j]:
                    case 1:
                        fresh_cnt += 1
                    case 2:
                        q.append((i,j))
        while q and fresh_cnt:
            for _ in range(len(q)):
                i, j = q.popleft()
                for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if -1 < r < m and -1 < c < n and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh_cnt -= 1
                        q.append((r,c))
            res += 1
        return res if not fresh_cnt else -1