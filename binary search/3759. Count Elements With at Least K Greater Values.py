class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        res = 0

        for i in range(N):
            l = bisect_right(nums, nums[i])
            r = bisect_right(nums, nums[-1])
            if r - l >= k:
                res += 1
        
        return res