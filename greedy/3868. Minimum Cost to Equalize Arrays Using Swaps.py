class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        n1 = Counter(nums1)
        n2 = Counter(nums2)
       
        res = 0

        for i, j in n1.items():
            diff = j - n2[i]
            if diff % 2:
                return -1
            if diff > 0:
                n2[i] = 0
                res += int(diff / 2)
            elif diff < 0:
                n2[i] = -1 * diff
            else:
                n2[i] = 0
               
        for j in n2.values():
            if j % 2:
                return -1

        return res
            
           