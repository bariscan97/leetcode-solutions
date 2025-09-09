class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        dic = Counter()
        j = 0
        res = 0
        for i in range(len(s)):
            dic[s[i]] += 1
            while not all(x < k for x in dic.values()):
                dic[s[j]] -= 1
                j += 1
            res += j
        return res