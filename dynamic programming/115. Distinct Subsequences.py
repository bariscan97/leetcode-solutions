class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @cache
        def dfs(i,j):
            
            if j == len(s) :
                if  i != len(t):
                    return 0
                return 1
            
            if i == len(t)  :
                return 1
            
            val = 0
            
            if t[i] == s[j]:
               
               val+=dfs(i+1,j+1)
            
            val += dfs(i,j+1)
            
            return val
        
        return dfs(0,0)