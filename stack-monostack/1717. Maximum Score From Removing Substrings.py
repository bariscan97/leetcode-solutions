class Solution:
    def calc(self,stack,x ,y):
            val = None
            cnt = 1
            for i in stack:
                if val is None:
                    val = i
                    continue
                if val == i :
                    cnt += 1
                else:
                    diff = len(stack) - cnt
                    if val == "b":
                        return min(cnt, diff) * y
                    else:
                        return  min(cnt ,diff) * x
            return 0
    
    def maximumGain(self, s: str, x: int, y: int) -> int:

        stack = []
        res = 0
        cnt = 0
        for i in s:
            if i != "a" and i != "b":
                res += self.calc(stack,x, y)
                stack = []
                continue
            if x > y:
                if stack and stack[-1] == "a" and i == "b":
                    stack.pop()
                    res += x
                    continue
            else:
                if stack and stack[-1] == "b" and i == "a":
                    stack.pop()
                    res += y
                    continue
            stack.append(i)

        res += self.calc(stack ,x, y)

        return res
        