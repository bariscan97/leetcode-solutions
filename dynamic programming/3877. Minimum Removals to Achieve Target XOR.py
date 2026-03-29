class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(i, bit):
            if i == len(nums):
                return -inf if bit != target else 0
            
            return max(
                dp(i + 1, bit ^ nums[i]) + 1,
                dp(i + 1, bit)
            )
        
        res = dp(0, 0)
        
        return len(nums) - res if res > -inf else -1