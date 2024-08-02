class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        N = len(colors)
        graph = defaultdict(list)
        indegree = [0] * N 
        
        for i ,j in edges:
            graph[i].append(j)
            indegree[j] += 1
        
        dic = {i : Counter(colors[i]) for i in range(N)}
        dp = {i : Counter() for i in range(N)}
        res = cnt = 0
        q = deque()
        
        for idx in range(N):
            if not indegree[idx] :
                q.append(idx)
        
        while q:
            node = q.popleft()
            cnt += 1
            if not graph[node]:
                res = max(res, max(dic[node].values()))
            for i in graph[node]:
                indegree[i] -= 1
                for k in dic[node].keys():
                    dp[i][k] = max(dp[i][k] ,dic[node][k])
                if not indegree[i]:
                    dic[i] += dp[i]
                    q.append(i)    
       
        return -1 if cnt != N else res