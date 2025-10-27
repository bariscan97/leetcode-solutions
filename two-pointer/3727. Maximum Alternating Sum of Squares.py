class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x:abs(x))
        res = 0
        l, r = 0, len(nums) - 1

        while r >= l:
            if r != l:
                res += nums[r] ** 2 - nums[l] ** 2
            else:
                res += nums[r] ** 2
            r -= 1
            l += 1
        
        return res