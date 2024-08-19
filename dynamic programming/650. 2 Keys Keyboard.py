class Solution:
    def minSteps(self, n: int) -> int:
        
        @cache
        def dp(total ,copy):
            if n == 1:
                return 0
            if total == n:
                return 1
            if total > n:
                return inf 
            
            return 1 + min(1 + dp(total + copy ,total + copy) , dp(total + copy ,copy))
       
        return dp(1 ,1)