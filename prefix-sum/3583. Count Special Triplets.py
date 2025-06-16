class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        N = len(nums)
        r_dic = Counter(nums)
        l_dic = Counter()
        res = 0
        MOD = 10 ** 9 + 7
        for i in range(N):
            r_dic[nums[i]] -= 1
            double_num = int(nums[i] * 2)
            z = l_dic[double_num]
            x = r_dic[double_num]
            val = int(z * x)
            l_dic[nums[i]] += 1
            res += val
        return res % MOD