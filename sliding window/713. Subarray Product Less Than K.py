class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        res = 0
        j = 0
        prods = 1
        for i in range(len(nums)) :
            
            prods *= nums[i]
            while j<=i and prods >= k:
                prods /= nums[j]
                j += 1
            res += (i -j) + 1

        
        return res