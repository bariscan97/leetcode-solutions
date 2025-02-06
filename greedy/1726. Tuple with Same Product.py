class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prods = Counter()
        N = len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                prods[nums[i] * nums[j]] += 1
        res = 0
        for k,v in prods.items():
           res += int(8 * (v - 1) * v / 2)
        return res