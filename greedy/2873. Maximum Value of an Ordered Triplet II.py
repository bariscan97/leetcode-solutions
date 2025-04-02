class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        left = nums[0]
        right = SortedList(nums[2:])
        res = 0
        for i in range(1, len(nums) -1):
            res = max(res, right[-1] * (left - nums[i]))
            left = max(left, nums[i])
            right.discard(nums[i + 1])
        return res