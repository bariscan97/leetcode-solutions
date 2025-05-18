class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])
        dic = defaultdict(list)
        visited = [[inf for j in range(n)] for i in range(m)]
        visited[0][0] = 0
        for i in range(m):
            for j in range(n):
                if not matrix[i][j] in ('.' ,'#'):
                    dic[matrix[i][j]].append((i,j))
        seens = set()
        q = deque()
        if matrix[0][0] in dic:
            seens.add(matrix[0][0])
            q.extend(dic[matrix[0][0]])
        else:
            q.append((0,0))
        cnt = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if (i,j) == (m - 1, n - 1):
                   return cnt
                paths =  [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]
                for r, c in paths:
                    if -1 < r < m and -1 < c < n and matrix[r][c] != '#' and not matrix[r][c] in seens:
                        if matrix[r][c] in dic:
                            seens.add(matrix[r][c])
                            for xx, yy in dic[matrix[r][c]]:
                                visited[xx][yy] = cnt 
                                q.append((xx,yy))
                        else:
                            if cnt < visited[r][c]:
                                visited[r][c] = cnt 
                                q.append((r,c))  
            cnt += 1 
        return -1
                        