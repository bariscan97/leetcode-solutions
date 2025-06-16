class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = max_val = -1
        for num in nums[::-1]:
            if max_val > num:
                res = max(res, max_val - num)
            max_val = max(max_val, num)
        return res