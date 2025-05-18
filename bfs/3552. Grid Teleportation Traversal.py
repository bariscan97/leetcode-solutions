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
        q = deque()
        q.append((0,0))
        visitedz = set()
        while q:
           
            i, j = q.popleft()
            if (i,j) == (m - 1, n - 1):
                return visited[i][j]
            paths =  [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]
            if matrix[i][j] in dic and not matrix[i][j] in visitedz:
                visitedz.add(matrix[i][j])
                for x,y in dic[matrix[i][j]]:
                    q.append((x,y))
            visited[i][j] += 1
            for r,c in paths:
                if -1 < r < m and -1 < c < n:
                    if not matrix[r][c] in ('.' ,'#'):
                        if matrix[i][j] != matrix[r][c]:
                            q.append((r,c))
                            aa = visited[i][j]
                            visited[r][c] =  aa
                            continue
                    if visited[i][j] <= visited[r][c]:
                        aa = visited[i][j]
                        visited[r][c] =  aa + 1
        print(visited)
        return -1
                        