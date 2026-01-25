class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        graph = defaultdict(list)

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        dic = {
            x: {},
            y: {},
            z: {},
        }
        
        def bfs(node):
            q = deque()
            q.append([node, 0])
            visited = set()

            while q:
                n, cnt = q.popleft()
                if n in visited:
                    continue
                visited.add(n)
                dic[node][n] = cnt
                for i in graph[n]:
                    q.append([i, cnt + 1])
                   
    
        bfs(x); bfs(y); bfs(z)
       
        res = 0
        
        for i in range(n):
            res += (
                dic[x][i] ** 2 + dic[y][i] ** 2 == dic[z][i] ** 2 or
                dic[x][i] ** 2 + dic[z][i] ** 2 == dic[y][i] ** 2 or
                dic[z][i] ** 2 + dic[y][i] ** 2 == dic[x][i] ** 2
            )
            
        return res