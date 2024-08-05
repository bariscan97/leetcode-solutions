class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        nodes = set([i for i in range(n)])
        
        for i, j in edges:
            if j in nodes:
                nodes.remove(j)
        
        return next(iter(nodes)) if len(nodes) == 1 else -1   