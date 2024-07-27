class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indgree = {i : 0 for i in range(numCourses)}
        graph = defaultdict(list) 
       
        for i ,j in prerequisites:
            graph[j].append(i)
            indgree[i] += 1
        q = deque()
        
        for i, j in indgree.items():
            if not j:
                q.append(i)
        
        if not q:
            return False
        
        course_cnt = 0
        
        while q:
            node = q.popleft()
            for i in graph[node]:
                indgree[i] -= 1
                if not indgree[i]:
                    q.append(i)
            course_cnt += 1
        
        return course_cnt == numCourses