class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        for i in nums:
            dp[i] = 0
        
        for i in nums:
            val = int(i ** 2)    
            if val in dp:
                dp[val] = max(dp[val], dp[i] + 1)
        
        res = max(dp.values())
        return -1 if not res else res + 1