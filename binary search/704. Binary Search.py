class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect_left(nums, target)
        if idx == len(nums) or nums[idx] != target:
            return -1 
        return idx