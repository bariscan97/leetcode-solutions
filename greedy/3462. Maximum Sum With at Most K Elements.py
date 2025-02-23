class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        if not k:return 0
        arr = []
        for i in range(len(grid)):
            if limits[i]:
                arr.extend(sorted(grid[i])[-limits[i]:])
        return sum(sorted(arr)[-k:])