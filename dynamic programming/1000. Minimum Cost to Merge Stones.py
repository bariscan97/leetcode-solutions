class Solution:
    def mergeStones(self, stones, k):
        n = len(stones)

        if (n-1)%(k-1): return -1

        ans = [0]

        for i in range(n):
            ans.append(ans[-1] + stones[i])

        @cache
        def dfs(lo,hi):
            if hi-lo+1 < k:
                return 0

            res = min(dfs(lo,i) + dfs(i+1,hi) for i in range(lo,hi,k-1))

            if (hi-lo)%(k-1) == 0:
                res += ans[hi+1] - ans[lo]

            return res

        return dfs(0,n-1)



