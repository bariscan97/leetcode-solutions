class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        res = 0
        tot = 0
        j = 0
       
        for i in range(len(nums)):
            
            tot += nums[i]
            
            while  nums[i] * ((i+1) -j ) - tot > k:
            
                tot -= nums[j]
                j += 1
 
            res = max(res, (i+1) - j)
       
        return res