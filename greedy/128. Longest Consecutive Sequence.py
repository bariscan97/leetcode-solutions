class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        prev = -1
        res = cnt = 0
        
        for curr in nums:
            if curr == prev + 1:
               cnt += 1
            else:
                cnt = 1
            prev = curr
            res = max(res, cnt)
        
        return res