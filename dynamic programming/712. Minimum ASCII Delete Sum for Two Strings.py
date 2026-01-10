class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        @cache
        def dp(i, j):
            if i == m or j == n:
                return 0
            
            if s1[i] == s2[j]:
                return dp(i + 1, j + 1) + ord(s1[i]) + ord(s2[j])
            
            return max(dp(i, j + 1), dp(i + 1, j))

        m = len(s1)
        n = len(s2)

        ordSum = sum([ord(i) for i in s1 + s2])
    
        return ordSum - dp(0,0)