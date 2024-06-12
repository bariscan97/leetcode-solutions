class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        inc_stack = []
        n = len(heights)
        ans = [0] * n

        for i in range(n - 1, -1, -1):
            total = 0

            while inc_stack and heights[i] > inc_stack[-1]:
                inc_stack.pop()
                total += 1
            
            if inc_stack:
                total += 1

            ans[i] = total
            inc_stack.append(heights[i])
        return ans