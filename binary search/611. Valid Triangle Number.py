class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        res = 0
        for i in range(N):
            for j in range(i + 1, N):
                mins = nums[i] + nums[j]
                left  = bisect_left(nums[j + 1:], nums[j])
                right = bisect_left(nums[j + 1:], mins)
                res += right - left
       
        return res