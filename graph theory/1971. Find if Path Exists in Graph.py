class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for i ,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        q = deque()
        q.append(source)
        visited = set()
       
        while q:
            node = q.popleft()
            if node in visited:
                continue
            if node == destination:
                return True
            visited.add(node)
            for i in graph[node]:
                q.append(i)
        
        return False