class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = Counter(p)
        dic = Counter()
        ok = {}
        N = len(s)
        j = 0 
        res = []
        for i in range(N):
            if not s[i] in p:
                dic.clear()
                j = i + 1
                ok = {}
                continue
            
            dic[s[i]] += 1
            
            if dic[s[i]] == p[s[i]]:
                ok[s[i]] = 1
            
            if len(ok) == len(p):
                res.append(j)
            
            while len(ok) == len(p) or dic[s[i]] > p[s[i]]:
                dic[s[j]] -= 1
                if dic[s[j]] != p[s[j]]:
                    if s[j] in ok:
                        del ok[s[j]]
                j += 1
        
        return res