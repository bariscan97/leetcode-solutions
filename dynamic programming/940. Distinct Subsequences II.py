class Solution:
    def distinctSubseqII(self, s: str) -> int:
        
        MOD = 10 ** 9 + 7
        
        @cache
        def dfs(ind):
            
            if ind == len(s):
                return 1
            
            my_set = set()
            val = 0
            
            for i in range(ind,len(s)):
                if not s[i] in my_set :
                   val += dfs(i+1)  
                my_set.add(s[i])
            
            return val + dfs(i+1)
        return (dfs(0) - 1) % MOD
        
        