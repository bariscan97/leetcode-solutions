class Solution:
    def maximumSwap(self, num: int) -> int:
        num = str(num)
        for i in range(len(num) - 1):
            arr = num[i+1:]
            max_val = max(arr)
            if arr and num[i] < max_val:
                idx = i + 1 + arr.rindex(max_val)
                num = num[:i] + num[idx] + num[i + 1:idx] + num[i] + num[idx+1:]
                break
        return int(num)
