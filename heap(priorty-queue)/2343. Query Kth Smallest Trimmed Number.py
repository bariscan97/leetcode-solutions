class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        for i ,j in queries:
            heap = []
            for idx in range(len(nums)):
                heappush(heap, [nums[idx][-j:] ,idx])
            for _ in range(i - 1):
                heappop(heap)
            res.append(heappop(heap)[1])
                
        return res