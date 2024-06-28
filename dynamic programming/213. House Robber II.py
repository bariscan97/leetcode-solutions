class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def dfs(start ,i):
            if i >= len(nums) or (start == 0 and i == len(nums) - 1 and len(nums) > 1):
                return 0
            return max(nums[i] + dfs(start,i + 2) , dfs(start, i + 1))
        
        return max([dfs(i,i) for i in range(len(nums))])