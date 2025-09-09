class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        uniques = len(set(nums))
        subs = Counter()
        res = j = 0
        for i in range(N):
            subs[nums[i]] += 1
            while len(subs) == uniques:
                res += N - i
                subs[nums[j]] -= 1
                if not subs[nums[j]]:
                    del subs[nums[j]]
                j += 1
        return res