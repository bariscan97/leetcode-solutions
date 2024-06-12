class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True
        @cache
        def dfs(i,j):
            if i == len(s) and j == len(p) :
                return True
            if i == len(s):
                if p[j] != "*":
                    return False
                return  dfs(i,j + 1)
            if j == len(p):
                return False
            if not p[j] in ("?", "*") and p[j] != s[i]:
                return False
            val = False
            if s[i] == p[j] or  p[j] == "?":
                val = val or dfs(i + 1,j + 1)
            if p[j] == "*":
                val = val or dfs(i ,j + 1)  or dfs(i + 1,j) 
            return val 
        
        
        return dfs(0,0)