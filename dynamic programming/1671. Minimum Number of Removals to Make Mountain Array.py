class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:

        def p_dfs(i):
            if i in prefix:
                return prefix[i]
            if i == -1:
                return 0
            val = 0
            for idx in range(i - 1, -1 , -1 ):
                if nums[idx] < nums[i]:
                    val = max(val ,p_dfs(idx))
            prefix[i] = 1 + val
            return prefix[i]
        
        def s_dfs(i):
            if i in suffix:
                return suffix[i]
            if i == len(nums):
                return 0
            val = 0
            for idx in range(i + 1,len(nums)):
                if nums[idx] < nums[i]:
                    val = max(val ,s_dfs(idx))
            suffix[i] = 1 + val
            return suffix[i]
        
        prefix ,suffix = dict() , dict()
        for i in range(len(nums)):
            s_dfs(i)
            p_dfs(i)
        max_val = 1
        for i in range(len(nums)):
            # print(prefix[i] ,"--- ",i," ---",suffix[i])
            if prefix[i] > 1 and suffix[i] > 1:
                max_val = max(max_val ,(prefix[i] + suffix[i]) - 1)
        
        return len(nums) - max_val