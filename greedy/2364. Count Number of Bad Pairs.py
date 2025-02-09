class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)
        dic = Counter()
        for i in range(N):
            dic[nums[i] - i] += 1
        return int((N * (N - 1)) / 2 - sum(((i - 1) * i) / 2 for i in dic.values()))