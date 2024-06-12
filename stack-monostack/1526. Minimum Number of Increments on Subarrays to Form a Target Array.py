class Solution:
    def minNumberOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) -1):
            if i == 0:
                res += nums[i]
            if nums[i + 1] > nums[i]:
                res += nums[i + 1] - nums[i]
        return res 