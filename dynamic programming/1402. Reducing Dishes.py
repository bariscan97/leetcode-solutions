class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        @cache
        def dp(i,time):
           
            if i == len(satisfaction):
                return 0
            return max(time * satisfaction[i] + dp(i + 1,time + 1), dp(i + 1,time))
        
        satisfaction.sort()
        
        return dp(0,1)