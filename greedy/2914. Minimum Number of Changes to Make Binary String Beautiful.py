class Solution:
    def minChanges(self, s: str) -> int:

        res = 0
        prev = None
        cnt = 0
        flag = False
        for i in s:
          
            if prev is None:
                cnt = 1
                prev = i
                continue
            if i != prev:
                if cnt % 2:
                    res += 1
                    prev = None
                    flag = True
                else:
                    prev = i
                    flag = False
                cnt = 1
            else:
                cnt += 1
       
        return res