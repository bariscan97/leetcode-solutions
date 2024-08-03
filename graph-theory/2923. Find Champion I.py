class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        m ,n = len(grid) ,len(grid[0])
        nodes = set([i for i in range(n)])
        
        for i in range(m):
            for j  in range(n):
                if grid[i][j]:
                    if j in nodes:
                        nodes.remove(j)
        
        return next(iter(nodes))