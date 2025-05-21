class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        stack = []
        res = [-1] * N
        for i in range(N):
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                res[idx] = nums[i]
            stack.append(i)
        arr = nums[:stack[-1]][::-1]
        while stack:
            idx = stack.pop()
            while arr and arr[-1] <= nums[idx]:
                arr.pop()
            if arr:
                res[idx] = arr[-1]
        return res