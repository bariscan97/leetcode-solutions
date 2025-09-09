from sortedcontainers import SortedList
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        sl = SortedList()
        res = 0
        j = 0
        for i in range(len(nums)):
            sl.add(nums[i])
            while sl[-1] - sl[0] > 2:
                sl.discard(nums[j])
                j += 1
            res += (i - j) + 1
        return res