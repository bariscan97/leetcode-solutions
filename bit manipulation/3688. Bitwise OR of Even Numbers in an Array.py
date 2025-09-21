class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if (num & 1) ^ 1:
                res |= num
        return res