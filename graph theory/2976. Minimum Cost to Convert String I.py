class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        N = len(original)
        
        graph = defaultdict(list)

        for i, j, c in zip(original, changed, cost):
            graph[i].append([j, c])
        
        
        @cache
        def bfs(src, desc):
            costs = {i: inf for i in ascii_lowercase}
            costs[src] = 0
            
            pq = []
            heappush(pq, [0, src])

            while pq:
                dist, node = heappop(pq)
                
                if node == desc:
                    return dist

                if dist > costs[node]:
                    continue

                for i, c in graph[node]:
                    if costs[i] >  costs[node] + c:
                        costs[i] = costs[node] + c
                        heappush(pq, [costs[i], i])
            
            return -1

        res = 0

        for i, j in zip(source, target):
            val = bfs(i,j)
            if val == -1:
                return -1
            res += val
        
        return res