class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        for x in arr:
            val = x - difference
            if val in dp:
                dp[x] = dp[val] + 1
            else:
                dp[x] = 1
        return max(dp.values())