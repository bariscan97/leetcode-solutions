class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def dfs(i):
            if i == len(s):
                return -1
           
            cut = float('inf')
            for j in range(i, len(s)):
                if s[i: j + 1] == s[i: j + 1][::-1]:
                    cut = min(cut, 1 + dfs(j + 1))
           
            return cut

        return dfs(0)