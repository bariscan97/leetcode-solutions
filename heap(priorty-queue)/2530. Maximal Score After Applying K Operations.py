class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        max_heap = [-i for i in nums]
        heapify(max_heap)
        for _ in range(k):
            val = heappop(max_heap) * (-1)
            res += val 
            heappush(max_heap, ceil(val / 3) * (-1))
        return res