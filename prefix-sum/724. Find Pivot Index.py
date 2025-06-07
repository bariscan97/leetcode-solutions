class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = nums[:]
        for i in range(1, N):
            prefix[i] += prefix[i - 1] 
        for i in range(N):
            right = prefix[i] - nums[i]
            left = prefix[N - 1] - prefix[i]
            if left == right:
                return i
        return -1