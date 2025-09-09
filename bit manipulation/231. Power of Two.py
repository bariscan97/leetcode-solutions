class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        val = 1
        while val <= n:
            if val == n:
                return True
            val <<= 1
        return False