class Solution:
    def numSub(self, s: str) -> int:
        res ,cnt = 0 , 0
        MOD = 10 ** 9 + 7
        for i in s:
            if i == "1":
                cnt += 1
                res += cnt
            else:
                cnt = 0
        return res % MOD
