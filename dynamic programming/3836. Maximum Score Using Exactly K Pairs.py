class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

        n, m = len(nums1), len(nums2)
        
        @cache
        def dp(i, j, cnt):

            if cnt == 0:
                return 0

            if i == n or j == m or n - i < cnt or m - j < cnt:
                return 0 if cnt == 0 else -inf
            
            return max(
                dp(i + 1, j + 1, cnt - 1) + nums1[i] * nums2[j],
                dp(i + 1, j, cnt),
                dp(i, j + 1, cnt)
            )
            
        dp.cache_clear()
        return dp(0, 0, k)