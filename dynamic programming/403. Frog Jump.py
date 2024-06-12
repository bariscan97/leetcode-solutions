class Solution:
    def canCross(self, stones: List[int]) -> bool:
       
        last_stone = stones[-1]
        stones = set(stones)
       
        @cache
        def dfs(val,k):
            nonlocal last_stone
            
            if val == last_stone:
                return True
            if k<1:
                return False
            if not val in stones:
                return False
            
            return dfs(val+k,k) if val == 0 else (dfs(val+(k-1),k-1) or dfs(val+k,k) or dfs(val+(k+1),k+1))
             
       
        return dfs(0,1)        