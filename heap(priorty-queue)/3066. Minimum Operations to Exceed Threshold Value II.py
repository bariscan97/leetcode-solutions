class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        size = len(nums)
        while True:
            x = heappop(nums)
            if x >= k:
                heappush(nums, x)
                break
            y = heappop(nums)
            heappush(nums,int(min(x, y) * 2 + max(x, y)))
        return size - len(nums)