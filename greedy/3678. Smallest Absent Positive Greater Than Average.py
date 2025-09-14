class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        A = set(nums)
        avg = sum(nums) / len(nums)
        for i in range(1,102):
            if i > avg and not i in A:
                return i 