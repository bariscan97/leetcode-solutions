class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = max_cnt = j = 0
        max_val = max(nums)
        N = len(nums)
        for i in range(N):
            if nums[i] == max_val:
                max_cnt += 1
            while max_cnt == k:
                res += N - i
                if nums[j] == max_val:
                    max_cnt -= 1
                j += 1
        return res