class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a = b = c = res = j = 0
        for i in range(len(s)):
            match s[i]:
                case "a": a += 1
                case "b": b += 1
                case "c": c += 1
            while a >= 1 and b >= 1 and c >= 1:
                match s[j]:
                    case "a": a -= 1
                    case "b": b -= 1
                    case "c": c -= 1
                j += 1
            res += j
        return res