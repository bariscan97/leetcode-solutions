class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        last_val = arr[-1]
        N = len(arr)
        l_idx = N - 2
        while l_idx >= 0 and last_val >= arr[l_idx]:
            last_val = arr[l_idx] 
            l_idx -= 1
        rArr = arr[l_idx + 1:]
        res = len(rArr)
        for i in range(N - 1):
            idx = bisect_left(rArr, arr[i])
            res = max(res, len(rArr) - idx + i + 1)
            if arr[i] > arr[i + 1] : 
                break
        return max(N - res, 0)