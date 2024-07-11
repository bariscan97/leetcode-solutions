class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        tot ,res = 0 ,0
        for i in nums:
            tot += i
            if tot < 0:
                tot = 0
            res = max(res, tot)
        tot = 0
        for i in nums:
            tot += i
            if tot > 0:
                tot = 0
            res = max(res ,abs(tot))
        return res