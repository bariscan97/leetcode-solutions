class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
     
        @cache
        def dfs(i, tot):
            if i == len(nums):
                return 1 if tot == target else 0
            return  dfs(i + 1, tot - nums[i]) + dfs(i + 1, tot + nums[i])
    
        return dfs(0,0)