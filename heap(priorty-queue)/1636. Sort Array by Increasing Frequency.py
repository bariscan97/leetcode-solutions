class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        arr = [[j,-i] for i ,j in Counter(nums).items()]
        heapify(arr)
        res = []
        while arr :
            cnt ,elem = heappop(arr)
            res.extend([-elem] * cnt)
        return res
            