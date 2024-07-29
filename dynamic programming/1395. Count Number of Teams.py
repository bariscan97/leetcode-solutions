class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        @cache
        def dp(i,cnt,go):
            if cnt == 2:
                return 1
            
            val = 0
            for idx in range(i + 1, N):
                if go :
                    if rating[i] < rating[idx]:
                        val += dp(idx ,cnt + 1 ,go)
                else:
                    if rating[i] > rating[idx]:
                        val += dp(idx ,cnt + 1 ,go)
            return val
       
        res = 0
        N = len(rating)
        go = True
        for _ in range(2):
            for i in range(N):
                res += dp(i, 0, go) 
            go = False
        
        return res