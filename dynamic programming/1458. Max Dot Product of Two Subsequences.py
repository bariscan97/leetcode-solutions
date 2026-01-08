class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def dp(i, j):
            if i == m or j == n:
                return -inf
            
            return max(
                dp(i + 1, j),
                dp(i, j + 1),
                max(dp(i + 1, j + 1), 0) + (nums1[i] * nums2[j])
            )

        m = len(nums1)       
        n = len(nums2)
        
        return dp(0,0)
        