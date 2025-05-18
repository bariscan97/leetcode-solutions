def digits_sum(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        sorted_nums =  sorted(nums, key = lambda x: [digits_sum(x), x])
        res = 0
        dic = {}
        for i in range(len(nums)):
            dic[sorted_nums[i]] = i
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                idx = dic[nums[i]]
                sorted_nums[i], sorted_nums[idx] = nums[i], sorted_nums[i]
                dic[nums[i]] = i
                dic[sorted_nums[idx]] = idx
                res += 1
        return res