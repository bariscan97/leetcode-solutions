class Solution:
    def decodeString(self, s: str) -> str:
        
        def f(i):
            num, res = "", ""

            while i < len(s):
                if "0" <= s[i] <= "9":
                    num += s[i]
                elif s[i] == "[":
                    rr, ii = f(i + 1)
                    res += int(num) * rr
                    num = ""
                    i = ii
                else:
                    if s[i] == "]":
                        break
                    res += s[i]
                i += 1
            
            return [res, i]

        res, _ = f(0)

        return res