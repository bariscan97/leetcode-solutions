class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:

        def f(i, n1 ,n2):
            if i == len(nums):
                return n1 == n2 == target
            return f(i + 1, n1 * nums[i], n2) or f(i + 1, n1 , n2 * nums[i])

        return f(0, 1, 1)