class Solution:
    def minimumSteps(self, s: str) -> int:
        zero_cnt = res = 0
        for i in range(len(s) -1, -1, -1):
            if s[i] == "0":
                zero_cnt += 1
            else:
                res += zero_cnt
        return res 