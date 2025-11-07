class Solution:
    def maximumLength(self, s: str) -> int:
        res = -1
        dic = Counter()
        prev = s[0]
        cnt = 1
        dic[(prev, cnt)] = 1
        
        for curr in s[1:]:
            if prev == curr:
                cnt += 1
            else:
                cnt = 1
            dic[(curr, cnt)] += 1
            dic[(curr, cnt - 1)] += 1
            dic[(curr, cnt - 2)] += 1
            prev = curr    

        for i, j in dic.items():
            if j >= 3:
                res = max(res, i[1])
        
        return res