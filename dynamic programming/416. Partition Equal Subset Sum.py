class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dp(curr,i):
            if i == len(nums):
                return curr == self.total / 2
            if curr > self.total / 2:
                return False
            if curr == self.total / 2:
                return True
            return dp(curr + nums[i], i + 1) or dp(curr, i + 1)
        self.total = sum(nums)
        nums.sort()
        return dp(0, 0)