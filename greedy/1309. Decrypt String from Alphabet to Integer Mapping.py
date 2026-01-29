class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = curr = ""
        
        for i in s:
            if i != "#":
                curr += i
            else:
                res += "".join([chr(int(j) + 96) for j in curr[:-2]]) + chr(int(curr[-2:]) + 96)
                curr = ""
        
        return res + "".join([chr(int(j) + 96) for j in curr])