class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i in range(len(nums)):
            while stack and stack[-1] > nums[i] and k - len(stack) <= (len(nums) - 1) - i :
                stack.pop()
            if len(stack) < k:
                stack.append(nums[i])
        return stack