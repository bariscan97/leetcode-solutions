class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        arr = [-i for i in gifts]; heapify(arr)
        for _ in range(k):heappush(arr, -1 * int(sqrt(heappop(arr) * (-1))))
        return sum(arr) * -1