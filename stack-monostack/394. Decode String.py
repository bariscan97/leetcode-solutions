class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        num =  val = ""
        for i in  s:
            if "0" <= i <= "9":
                num += i
            elif i == "[":
                stack.append([int(num), val])
                num =  val = ""
            elif i == "]":
                a, b = stack.pop()
                b += a * val
                val = b
            else:
                val += i
    
        return val