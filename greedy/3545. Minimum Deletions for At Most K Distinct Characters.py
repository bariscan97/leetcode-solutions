class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        arr = sorted([i for i in Counter(s).values()])
        N = len(arr)
        res = 0
        for i in range(N):
            if N - 1 - i < k:
                break
            res += arr[i]
        return res