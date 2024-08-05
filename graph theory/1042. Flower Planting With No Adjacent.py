class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        colors = [0 for i in range(n)]
        for i ,j in paths:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(node):
            if colors[node - 1]:
                return
            for num in range(1, 5):
                if not num in [colors[idx - 1] for idx in graph[node]]:
                    colors[node - 1] = num
                    break
            for i in graph[node]:
                dfs(i)
                            
        for i in range(1,n + 1):
            dfs(i)
        
        return colors
                    