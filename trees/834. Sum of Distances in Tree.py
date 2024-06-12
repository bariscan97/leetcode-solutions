from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        count = [0] * N
        res = [0] * N
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs1(cur: int, parent: int) -> None:
            count[cur] = 1
            for child in graph[cur]:
                if child != parent:
                    dfs1(child, cur)
                    count[cur] += count[child]
                    res[cur] += res[child] + count[child]
        
        def dfs2(cur: int, parent: int) -> None:
            for child in graph[cur]:
                if child != parent:
                    res[child] = res[cur] + N - 2 * count[child]
                    dfs2(child, cur)
        
        dfs1(0, -1)
        dfs2(0, -1)
        
        return res