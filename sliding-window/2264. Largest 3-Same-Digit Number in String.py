class Solution:
    def largestGoodInteger(self, num: str) -> str:
        curr = res = ""
        for i in range(len(num)):
            if curr and curr[-1] != num[i]:
                curr = ""
            curr += num[i]
            if len(curr) == 3:
                res = max(res, curr)
                curr = curr[1:]
        return res