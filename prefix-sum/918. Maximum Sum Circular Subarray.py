class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        N = len(nums)
        suffix = nums[:]
        tot = 0
        val = -inf
        
        for i in range(N - 1,-1, -1):
            tot += suffix[i]
            val = max(val ,tot)
            suffix[i] = val
       
        kadane = total = 0
        res = -inf
        for i in range(N):
            kadane += nums[i]
            total += nums[i]
            
            if total > 0:
                res = max(res ,suffix[i + 1] + total if i < len(suffix) - 1 else total)
        
            res = max(res ,kadane)
            
            if kadane < 0:
                kadane = 0
        
     
        return res