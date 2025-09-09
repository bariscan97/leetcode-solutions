class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        
        overloops , min_arr = [], []
        j = 0
        total = 0
        for i in range(len(arr)):
            total += arr[i]
            while total > target:
                total -= arr[j]     
                j += 1
            if total == target:
                overloops.append([j, i, (i - j) + 1])
                min_arr.append((i - j) + 1)
        res = inf 
        for i in range(len(min_arr) - 2, -1, - 1):
            min_arr[i] = min(min_arr[i], min_arr[i + 1])
        for i in range(len(overloops)):
            end = overloops[i][1]
            idx = bisect_left(overloops,[end + 1,end + 1,0] )
            if idx < len(overloops):
                res = min(res,overloops[i][2] + min_arr[idx]) 
        
        return res if res < inf else -1
            