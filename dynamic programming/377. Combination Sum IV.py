class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def dp(total):
            res = 0
            for num in nums:
                if total + num == target:
                    res += 1
                if total + num < target:
                    res += dp(total + num)
            return res

        return dp(0)