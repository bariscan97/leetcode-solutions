from sortedcontainers import SortedList
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sl , res = SortedList(nums[1:]) , 0
        for i in range(1,len(nums)):
            res +=  sl.bisect_right(upper - nums[i - 1]) - sl.bisect_left(lower - nums[i - 1]) 
            sl.discard(nums[i])
        return res