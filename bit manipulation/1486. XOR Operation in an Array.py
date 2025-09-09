class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = [start + 2 * i for i in range(n)]
        res = 0
        for i in arr:
            res ^= i
        return res  
    