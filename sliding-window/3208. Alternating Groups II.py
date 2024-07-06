class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N = len(colors) + (k - 1)
        prev = None
        MOD = len(colors)
        cnt = 1
        res = 0
        for i in range(N):
            if prev is None:
                prev = colors[i % MOD]
                continue
            if prev != colors[i % MOD]:
                if cnt < k :
                    cnt += 1
            else:
                cnt = 1
            prev = colors[i % MOD]
            if cnt == k:
                res += 1
        return res