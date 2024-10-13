class Solution:
    def countWinningSequences(self, s: str) -> int:
        
        dic = {
            "F" : "E" ,
            "W" : "F",
            "E" : "W"
        }
        
        @cache
        def dp(prev, total, i):
            if i == len(s):
                return 1 if total > 0 else 0
          
            val = 0
            for c in ["E","F","W"]:
                if c == prev :
                    continue
                if c == dic[s[i]]:
                    val += dp(c, total - 1,  i + 1)
                if c != dic[s[i]] and  dic[c] != s[i] :
                    val += dp(c, total,  i + 1)
                if dic[c] == s[i]:
                    val += dp(c, total + 1,  i + 1)
            return val
       
        return dp(None,0,0) % (10 ** 9 + 7)