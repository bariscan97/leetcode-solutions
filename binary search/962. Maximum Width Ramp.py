class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(nums)):
            if len(stack) == 0:
                stack.insert(0, [nums[i], i])
                continue
            if nums[i] < stack[0][0]:
                stack.insert(0, [nums[i], i])
            else:
                idx = bisect_left(stack, [nums[i], i])
                if idx == len(stack):
                    res = max(res, i)
                else:
                    res = max(res, (i - stack[idx -1 if idx > 0 else idx][1]))
        return res