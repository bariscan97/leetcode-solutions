from sortedcontainers import SortedList
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sl = SortedList(nums[1:])
        res = 0
        for i in range(1, len(nums)):
            idx = sl.bisect_left(nums[i - 1] / 2)
            sl.discard(nums[i])
            res += idx
        return res