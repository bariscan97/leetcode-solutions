def digits_sum(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if digits_sum(nums[i]) == i:
                return i
        return -1