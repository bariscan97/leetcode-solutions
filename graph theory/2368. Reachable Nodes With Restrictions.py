class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            val = 0
            for i in dic[node]:
                val += dfs(i)
            return val + 1
        
        dic = defaultdict(list)
        
        for i ,j in edges:
            dic[i].append(j)
            dic[j].append(i)
        
        visited = set(restricted)
        
        return dfs(0)