class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        @cache
        def dfs(node, parent):
            if node == parent:
                return True
            val = False
            for i in graph[node]:
                val = val or dfs(i,parent)
            return val
        
        graph = defaultdict(list)
        res = []
        
        for i, j in prerequisites :
            graph[i].append(j)
        
        for u ,v in queries:
            res.append(dfs(u,v))
            
       
        return res