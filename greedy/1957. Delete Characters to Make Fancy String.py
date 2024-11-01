class Solution:
    def makeFancyString(self, s: str) -> str:
        cnt = 1
        res = curr = s[0]
        for i in s[1:]:
            if i == curr:
                cnt += 1
            else:
                curr = i
                cnt = 1
            if cnt < 3:
                res += i
        return res
        