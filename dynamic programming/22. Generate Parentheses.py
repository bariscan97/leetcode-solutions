class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(l,r,s):
            if r + l == 2 * n:
                res.append(s)
            if l < n:
                dfs(l+1,r,s+"(")
            if l > r:
                dfs(l,r+1,s+")")
        dfs(0,0,"")
        return res