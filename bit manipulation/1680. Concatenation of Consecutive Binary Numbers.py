class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        res = bits = 0
        for num in range(1, n + 1):
            if num & (num - 1) == 0:
                bits += 1
            res = ((res << bits) + num) % MOD
        return res
