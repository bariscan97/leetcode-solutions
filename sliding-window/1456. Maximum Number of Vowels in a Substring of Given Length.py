class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        N = len(s)
        res = cnt = 0
        for i in range(N):
            if s[i] in vowels:
                cnt += 1
            if i >= k - 1:
                res = max(res, cnt)
                if s[i - (k - 1)] in vowels:
                    cnt -= 1
        return res