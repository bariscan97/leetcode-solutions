class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def helper(n):
            if n == 1:
                return 1 
            if n == 2:
                return 2
            return helper(n-2) + helper(n-1)
        return helper(n)
    