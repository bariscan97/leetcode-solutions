class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        
        @cache
        def dfs(i, prev1, prev2):
            if i == len(nums):
                return 1 
            val = 0
            for idx in range(nums[i] + 1):
                if prev1 != None and prev2 != None:
                    if idx >= prev1 and (nums[i] + 1) - idx <= prev2:
                        val += dfs(i + 1, idx, (nums[i] + 1) - idx)
                else:
                    val += dfs(i + 1, idx, (nums[i] + 1) - idx)
            return val 
            
        return dfs(0,None,None) % (10 ** 9 + 7 )