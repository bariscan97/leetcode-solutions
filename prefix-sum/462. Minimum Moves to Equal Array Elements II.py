class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        prefix = [0] * N
        total = sum(nums)
        val = 0 
        res = inf
        
        for i in range(N):
           
            val += nums[i]
            prefix[i] = val
            diff = (N - 1) - i
            suff = (total - prefix[i]) - nums[i] * diff 
            preff = nums[i] * (i + 1)  - prefix[i]
            res = min(res , suff + preff)
       
        return res