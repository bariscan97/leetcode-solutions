class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0] * n
        graph = defaultdict(list)
        pathSum = defaultdict(int)
        res = 0
        
        for i ,j in relations:
            graph[i].append(j)
            indegree[j - 1] += 1
       
        for i in range(1 ,n + 1):
            pathSum[i] = 0
            if not i in graph:
                res = max(res, time[i - 1])
        q = deque()
       
        for i in range(n):
            if not indegree[i]:
                pathSum[i + 1] = time[i]
                q.append(i + 1)
        
        while q:
            
            node = q.popleft()
    
            for i in graph[node]:
                indegree[i - 1] -= 1
                pathSum[i] = max(pathSum[i] ,pathSum[node])
                if not indegree[i - 1]:
                    pathSum[i] += time[i - 1]
                    res = max(res, pathSum[i])
                    q.append(i) 
       
        return res