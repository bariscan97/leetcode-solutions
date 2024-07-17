class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for idx in range(len(isConnected[i])):
                if isConnected[i][idx] :
                    dfs(idx) 
        visited = set()
        res = 0
        for index in range(len(isConnected)):
            if index in visited:
                continue
            res += 1
            dfs(index)
        
        return res