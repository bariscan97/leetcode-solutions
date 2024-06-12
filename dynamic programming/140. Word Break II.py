class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        word_dict = set(wordDict)
        res = []
        
        def dfs(i,string,subs):
            nonlocal res
            if len(string)>=10:
                return
            if i == len(s):
                if string == "":
                    res.append(subs[:-1])
                return
            if string + s[i] in word_dict:
                dfs(i+1,"",subs + string+s[i]+ " ")
            dfs(i+1,string+s[i],subs)
        
        dfs(0,"","")
        
        return res