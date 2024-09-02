class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        
        @cache
        def dfs(i, prev):
            if i == len(nums):
                return 1 
            val = 0
            start = 0
            if i:
                if nums[i] >= nums[i - 1]:
                    start = prev

            for idx in range(start, nums[i] + 1):
                if i:
                    if idx >= prev and nums[i] - idx <= nums[i - 1] - prev:
                        val += dfs(i + 1, idx)
                else:
                    val += dfs(i + 1, idx)
            return val 
            
        return dfs(0,None) % (10 ** 9 + 7 )