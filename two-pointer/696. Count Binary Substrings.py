class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        N = len(s)
        res = one = zero = 0
        prev = None
        
        for i in range(N):
            if s[i] == "1":
                if prev != s[i]:
                    res += min(one, zero)    
                    one = 0
                one += 1
            else:
                if prev != s[i]:
                    res += min(one, zero)    
                    zero = 0    
                zero += 1
            prev = s[i]
           
        return res + min(one, zero)
        