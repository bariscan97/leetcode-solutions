class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        
        @cache
        def dp(i, j) :
            if j == len(b):
                return 0 if i == 4 else -inf
            if i == 4:
                return 0
            return max(dp(i ,j + 1), b[j] * a[i] + dp(i + 1, j + 1)) 
        
        return dp(0,0)