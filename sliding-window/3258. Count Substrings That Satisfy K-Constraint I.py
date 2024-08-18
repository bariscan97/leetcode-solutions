class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res = 0
        dic = {"0" : 0 , "1" : 0}
        j = 0
        for i in range(len(s)):
            dic[s[i]] += 1
            while dic["1"] > k and dic["0"] > k:
                dic[s[j]] -= 1
                j += 1
            res += (i - j) + 1 
        
        return res