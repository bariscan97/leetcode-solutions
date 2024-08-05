class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {i : 0 for i in range(numCourses)}
        graph = defaultdict(list) 
        
        for i ,j in prerequisites:
            graph[j].append(i)
            indegree[i] += 1
       
        q = deque()
        res = []
        
        for i, j in indegree.items():
            if not j:
                res.append(i)
                q.append(i)
        
        while q:
            node = q.popleft()
            for i in graph[node]:
                indegree[i] -= 1
                if not indegree[i]:
                    res.append(i)
                    q.append(i)
        
        return res if all(i == 0 for i in indegree.values()) else []