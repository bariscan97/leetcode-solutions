class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        def bfs():
            q = deque()
            q.append([0,0])
            visited = set()
            while q:
                cnt ,node = q.popleft()
                if node in visited:
                    continue
                if node == n - 1:
                    return cnt
                visited.add(node)
                for i in graph[node]:
                    q.append([cnt + 1, i])
        
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append(i + 1)
        
        res = []
        for i, j  in queries:
            graph[i].append(j) 
            res.append(bfs())
        
        return res
            
            