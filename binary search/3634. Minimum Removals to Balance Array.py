class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        max_size = 0
        for i in range(N):
            idx = bisect_right(nums, nums[i] * k) 
            max_size = max(max_size, idx -i)
        return N - max_size