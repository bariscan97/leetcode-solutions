class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = inf
        total = 0
        j = 0
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                res = min(res,(i - j) + 1)
                total -= nums[j]
                j += 1
        return res if res < inf else 0