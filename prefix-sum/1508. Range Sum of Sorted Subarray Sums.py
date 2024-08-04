class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        prefix = nums[:]
        N = len(nums)
        MOD = 10 ** 9 + 7
        sl = []
       
        for i in range(1 ,N):
            prefix[i] += prefix[i - 1]
        
        for i in range(N):  
            sl.append(prefix[i])
            for j in range(i):
                sl.append(prefix[i] - prefix[j])
        
        res = 0
        sl.sort()
        
        for i in sl[left - 1 : right]:
            res += i
            res %= MOD
        
        return res
        
        