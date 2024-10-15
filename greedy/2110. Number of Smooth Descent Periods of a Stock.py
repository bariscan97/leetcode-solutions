class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res  = cnt = 1
        prev = prices[0]
        for curr in prices[1:]:
            cnt = cnt + 1 if curr + 1 == prev else 1
            res += cnt
            prev = curr
        return res