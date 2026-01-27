class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        costs = {i:inf for i in range(n)}

        for i, j, c in edges:
            graph[i].append([j, c])
            graph[j].append([i, c * 2])

        q = deque()
        q.append(0)

        costs[0] = 0

        while q:
            node = q.popleft()
            for i, c in graph[node]:
                t = costs[node] + c 
                if t < costs[i]:
                    costs[i] = t
                    q.append(i)
            
        
        return costs[n-1] if costs[n - 1] < inf else -1