class Solution:
    def maxScore(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return int(nums[0] ** 2)
        res = lcm(*nums) * gcd(*nums)
        for i in range(len(nums)):
            arr = nums[:i] + nums[i+1:]
            res = max(res,lcm(*arr) * gcd(*arr))
        return res 