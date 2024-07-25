class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        graph = defaultdict(list)
        
        for i in range(len(parent)):
            if parent[i] == -1:
                continue
            graph[parent[i]].append(i)
     
        def dfs(idx):
            nonlocal res
            val = 0
            arr = []
            for i in graph[idx]:
                A = dfs(i)
                if s[idx] != s[i]:
                    val = max(val, A)     
                    heappush(arr, -A)
            left_right = 0
            for _ in range(2):
                if arr:
                    left_right += heappop(arr) * (-1)
            res = max(res ,left_right + 1)
            return val + 1
        
        res = 0
        dfs(0)
       
        return res