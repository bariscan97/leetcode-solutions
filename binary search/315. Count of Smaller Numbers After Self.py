from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl = SortedList(nums[1:])
        res = [0] * len(nums)
        for i in range(1,len(nums)):
            idx = sl.bisect_left(nums[i - 1] - 1/2)
            sl.discard(nums[i])
            res[i - 1] = idx
        return res
        