class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for i, j, c in flights:
            graph[i].append([j, c])

        costs = [inf] * n
        costs[src] = 0

        q = deque()
        q.append((src, 0, 0))
        
        while q:
            u, cnt, cost = q.popleft()
            
            for i, c in graph[u]:
                t = cost + c 
                
                if t < costs[i] and cnt <= k:
                    costs[i] = t
                    q.append((i, cnt + 1, cost + c))
        
        
        return costs[dst] if costs[dst] < inf else -1