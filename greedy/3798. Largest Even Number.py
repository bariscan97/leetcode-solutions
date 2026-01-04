class Solution:
    def largestEven(self, s: str) -> str:
        for i in range(len(s)-1, -1, -1):
            if s[i] == "2":
                return s[:i + 1]
        return ""