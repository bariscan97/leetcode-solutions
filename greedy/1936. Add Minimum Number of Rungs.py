class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        res = prev = 0
        for curr in rungs:
            diff = curr - prev
            if diff > dist:
                res += (diff - 1) // dist
            prev = curr
        return res