class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        @cache
        def dp(i ,A ,B):
            if A < 0 or B < 0:
                return inf
            if i == len(costs):
                return 0 
            return min(costs[i][0] + dp(i + 1, A - 1, B), costs[i][1] + dp(i + 1, A, B - 1))
        N = int(len(costs) / 2)
        return dp(0 ,N ,N)