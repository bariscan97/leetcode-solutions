class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        
        @cache
        def dp(i):  
            if i == len(costs) - 1:
                return costs[0]
            val = inf
            if i + 1 < len(costs):
                val = min(val, dp(i + 1) + costs[i + 1] + 1)
            if i + 2 < len(costs):
                val = min(val, dp(i + 2) + costs[i + 2] + 4)
            if i + 3 < len(costs):
                val = min(val, dp(i + 3) + costs[i + 3] + 9)
            return val
        
        costs = [0] + costs
        return dp(0)