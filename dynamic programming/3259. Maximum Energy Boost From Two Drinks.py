class Solution:
    def maxEnergyBoost(self, A: List[int], B: List[int]) -> int:
        @cache
        def dp(i,rot):
            if i == len(A):
                return 0
            if rot:
               return max(A[i] + dp(i + 1,rot), dp(i + 1,not rot))
            return max(dp(i + 1,not rot), B[i] + dp(i + 1,rot))
        return max(dp(0,True) ,dp(0, False))