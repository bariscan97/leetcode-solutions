class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        stack.append(-1)

        counter = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    counter = max(counter, i - stack[-1])
        return counter