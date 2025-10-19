class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        numSet = set(nums)
        val = k
        while True:
            if not val in numSet:
                return val
            val += k
        return -1