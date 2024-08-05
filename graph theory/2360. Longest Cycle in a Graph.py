class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        N = len(edges)
        graph = defaultdict()
        visited = set()
        cycle = [-1 for i in range(N)]
        res = -1
        
        for i in range(N):
            if edges[i] != -1:
                graph[i] = edges[i]
        
        def dfs(node, cnt):
            nonlocal res
            if node in visited and cycle[node] == -1:
                return
            if node not in graph:
                return 
            if cycle[node] > -1:
                
                res = max(res ,cnt - cycle[node])
                go = False
                return
            
            cycle[node] = cnt
            visited.add(node)
            
            dfs(graph[node] ,cnt + 1)
            
            cycle[node] = -1
        
        
        for i in range(N):
            dfs(i, 0)
        
        return res
        
            