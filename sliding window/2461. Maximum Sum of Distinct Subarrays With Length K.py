class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        dic = Counter()
        j = total = res = 0
        for i in range(len(nums)):
            dic[nums[i]] += 1
            total += nums[i]
            while dic[nums[i]] > 1 or i - j == k:
                dic[nums[j]] -= 1
                total -= nums[j]
                j += 1
            if i - j == k - 1:
                res = max(res ,total)
        return res