class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        dic = Counter(nums)

        for i in nums:
            if not i % 2 and dic[i] == 1:
                return i

        return -1