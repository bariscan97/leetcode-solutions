class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=set()
        size=len(s)
        def dfs(ind,string):
            if len(string)==size:
                res.add(string)
                ind-=1
                return 
            dfs(ind+1,string+s[ind].upper())
            dfs(ind+1,string+s[ind].lower())
        dfs(0,"")
        return [*res]