class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = nums[:]
        N = len(nums)
        res = -inf
        for i in range(1,N):
            prefix[i] += prefix[i - 1]
        dic = {}
        for i in range(len(nums)):
            idx = i % k
            if idx in dic:
                val = max(
                    dic[idx] + (prefix[i] - prefix[i - k]),
                    prefix[i] - prefix[i - k]
                )
                res = max(res, val)
                if val < 0:
                    val = 0
                dic[idx] = val
            else:
                dic[idx] = 0
                if i == k - 1:
                    res = max(res, prefix[i])
                    dic[idx] = prefix[i]
        return res
