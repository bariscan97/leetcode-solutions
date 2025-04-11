class Solution:
    def isValid(self, s: str) -> bool:
        t = ""
        for i in s:
            t += i
            if t[-3:] == "abc":
                t = t[:-3]
        return not t