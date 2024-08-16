from sortedcontainers import SortedList
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if not k:
            return max(vals)
        totals = Counter()
        res = max(vals) 
        graph = dict()
        for i in range(len(vals)):
            graph[i] = SortedList()
        for i, j in edges:
            if len(graph[i]) == k and  graph[i][0] < vals[j]:
                elem = graph[i].pop(0)
                totals[i] -= elem
            if len(graph[i]) < k and vals[j] > 0:
                totals[i] += vals[j]
                graph[i].add(vals[j])
            if len(graph[j]) == k and  graph[j][0] < vals[i]:
                elem = graph[j].pop(0)
                totals[j] -= elem
            if len(graph[j]) < k and vals[i] > 0:
                graph[j].add(vals[i])
                totals[j] += vals[i]
            res = max(res, vals[i] + totals[i], vals[j] +totals[j])
        
        return res