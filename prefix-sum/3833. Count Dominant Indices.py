class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        total = sum(nums)
        res = 0
        N = len(nums)

        for i in range(N - 1):
            total -= nums[i]
            res += nums[i] > total / (N - (i + 1)) 

        return res