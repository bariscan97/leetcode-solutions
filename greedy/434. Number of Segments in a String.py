class Solution:
    def countSegments(self, s: str) -> int:
        res = 0
        flag = False
        for i in s:
            if i != " ":
                if not flag:
                    res += 1
                flag = True
            else:
                flag = False
        return res