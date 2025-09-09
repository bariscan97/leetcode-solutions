class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while x or y:
            a = x & 1
            b = y & 1
            x >>= 1
            y >>= 1
            res += a ^ b
        return res  