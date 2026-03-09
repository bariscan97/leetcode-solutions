class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        res = [inf, inf]
        
        for i in range(len(capacity)):
            if capacity[i] >= itemSize and res[1] > capacity[i]:
                res = [i, capacity[i]]
           
        return res[0] if res[0] < inf else -1