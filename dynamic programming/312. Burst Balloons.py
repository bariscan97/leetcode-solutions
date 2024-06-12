class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + [num for num in nums if num != 0] + [1]
        dp = [[0] * len(nums) for _ in range(len(nums))]

        for r in range(2, len(nums)):
            for l in reversed(range(r - 1)):
                adj = nums[l] * nums[r]
                dp[l][r] = max( 
                    dp[l][i] + (adj * nums[i]) + dp[i][r] for i in range(l + 1, r)
                )
        return dp[0][-1]