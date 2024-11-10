class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        cnt = prev_cnt = 1
        prev = nums[0]
        res = 1
        for num in nums[1:]:
            if num > prev:
                cnt += 1
                if not cnt % 2:
                    res = max (res, int(cnt / 2))
                res = max(res, min(prev_cnt, cnt))
            else:
                prev_cnt = cnt
                cnt = 1
            prev = num
        return res