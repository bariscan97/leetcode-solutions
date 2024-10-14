class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        arr = [-a, -b, -c]
        heapify(arr)
        res = 0
        while True:
            val1 = heappop(arr)
            val2 = heappop(arr)
            if not val1 or not val2:
                break
            res += 1
            heappush(arr, val1 + 1 if val1 != 0 else val1)
            heappush(arr, val2 + 1 if val2 != 0 else val2)
        return res