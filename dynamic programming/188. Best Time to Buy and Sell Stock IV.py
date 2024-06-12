class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        @cache
        def dfs(first,k,i):
            
            if i == len(prices):
                return 0
            
            if k == 1 and first != None:
                if prices[i] > first:
                    return max(prices[i] - first,dfs(first,k,i+1))
               
            if first is None:
                return dfs(prices[i],k,i+1)
            else:
                
                val = 0
                if prices[i] > first :
                    return max((prices[i] - first) + dfs(None,k-1,i+1),dfs(first,k,i+1))
                return dfs(prices[i],k,i+1)
        
        return dfs(None,k,0)