class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res ,total ,j = 0 , 0 , 0
        for i in range(len(nums)):
            total += nums[i]
            while total * ((i - j) + 1) >= k:
                total -= nums[j]
                j += 1
            res += (i - j) + 1
        return res