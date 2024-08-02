class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @cache
        def dfs(i, j, k):
            if k == len(s3) :
                return i == len(s1) and j == len(s2) 
            val = False
            if i< len(s1) and s1[i] == s3[k]:
                val = val or dfs(i + 1,j,k + 1)
            if j < len(s2) and s2[j] == s3[k]:
                val = val or dfs(i,j + 1,k + 1)
    
            return  val
        
        return dfs(0,0,0)