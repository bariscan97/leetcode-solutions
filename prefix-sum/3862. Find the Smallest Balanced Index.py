class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        N = len(nums)
       
        sums = nums[:]

        for i in range(1, N):
            sums[i] += sums[i - 1]

        p = 1
        for i in range(N - 1, -1, -1):
            
            if i == N - 1:
                if sums[i] - nums[i] == 1:
                    return i
            elif sums[i] - nums[i] == p:
                return i
         
            p *= nums[i]
        
        return -1
            