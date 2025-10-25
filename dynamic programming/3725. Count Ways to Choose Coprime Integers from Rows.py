class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        
        @cache
        def dp(i, curr):
            if i == m:
                return curr == 1
            val = 0
            for c in range(n):
                val += dp(i + 1, gcd(mat[i][c], curr)) 
            return val 

        MOD = 10 ** 9 + 7
        res = 0
        
        m = len(mat)
        n = len(mat[0])
        
        for i in range(n):
            res += dp(1, mat[0][i])
        
        return res % MOD