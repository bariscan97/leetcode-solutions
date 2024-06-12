class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        dic = Counter()
        res = Counter()
        j = 0
        for i in range(len(s)):
            dic[s[i]] += 1
            while len(dic) > maxLetters:
                dic[s[j]] -= 1
                if dic[s[j]] == 0:
                    dic.pop(s[j])
                j += 1
           strs = ""
            for ii in range(i, j -1 , -1):
                strs = s[ii] + strs
                if len(strs) >= minSize:
                    res[strs] += 1
            
        # print(res)
        return max(res.values()) if res else 0
       