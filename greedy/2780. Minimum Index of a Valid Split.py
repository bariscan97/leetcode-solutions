class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        all_nums = Counter(nums)
        dic = Counter()
        N = len(nums)
        for i in range(N):
            all_nums[nums[i]] -= 1
            dic[nums[i]] += 1
            if dic[nums[i]] > (i + 1) / 2 and all_nums[nums[i]] > (N - i - 1) / 2:
                return i
        return -1