class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val ,max_val = arrays[0][0] , arrays[0][-1]
        res = 0
        for i in range(1, len(arrays)):
            res = max(res ,arrays[i][-1] - min_val ,max_val - arrays[i][0])
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        return res