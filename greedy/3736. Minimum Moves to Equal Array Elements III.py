class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return len(nums) * max(nums) - sum(nums)