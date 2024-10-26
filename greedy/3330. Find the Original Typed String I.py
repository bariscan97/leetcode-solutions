class Solution:
    def possibleStringCount(self, word: str) -> int:
        
        cnt = 1
        prev = word[0]
        res = 0
        for i in word[1:]:
            if i == prev:
                cnt += 1
            else:
                print(cnt)
                res += cnt - 1
                cnt = 1
                
            prev = i
        res += cnt
       
        return res