class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                idx = stack.pop()
                s = s[:idx + 1] + s[idx+1: i][::-1] + s[i:]
        return "".join([i for i in s if i != "(" and i != ")"])
        