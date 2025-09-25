class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @cache
        def dp(i,j):
            if i == len(triangle):
                return 0
            val = dp(i + 1, j)
            if i < len(triangle[i]):
                val = min(val, dp(i + 1, j + 1))
            return val + triangle[i][j]
        
        return dp(0,0)