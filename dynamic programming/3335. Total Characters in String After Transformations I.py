class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        
        @cache
        def f(cnt ,rem):
            if rem == 26:
                cnt += 1
                rem = 0
            if rem < 26 and not cnt:
                return 1
            return f(cnt - 1, rem) + f(cnt - 1, rem + 1) 
        
        MOD = 10 ** 9 + 7
        res = 0

        for i in s:
            x = ord(i) - 97
            tot = x + t
            a = tot // 26
            b = tot % 26
            res += f(a,b)

        return res % MOD 