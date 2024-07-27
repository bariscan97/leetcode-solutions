class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        indgree = {i :0 for i in range(n)}
        grandparents = defaultdict(set)
        for i ,j in edges:
            graph[i].add(j)
            grandparents[j].add(i)
            indgree[j] += 1
        q = deque()
        for i ,j in indgree.items():
            if not j:
                q.append(i)
       
        while q:
            node = q.popleft()
            for i in graph[node]:
                grandparents[i].update(grandparents[node])
                indgree[i] -= 1
                if not indgree[i] :
                    q.append(i)
        
        return [sorted(grandparents[i]) for i in range(n)]