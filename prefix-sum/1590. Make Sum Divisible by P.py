class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        N = len(nums)
        res = inf
        suffix = nums[:]
        prefix = nums[:]
        dic = defaultdict(list)
        
        suffix[-1] %= p
        prefix[0] %= p
        dic[nums[-1] % p].append(N - 1)

        for i in range(N - 2, -1, -1):
            suffix[i] = (nums[i] + suffix[i + 1]) % p
            if suffix[i] == 0:
                res = min(res, i)
            dic[suffix[i]].append(i)
        
        for i in range(1, N):
            prefix[i] = (nums[i] + prefix[i - 1]) % p
        
        for i in range(N):
            
            dic[suffix[i]].pop()
            if prefix[i]:
                v = p - prefix[i]
                if v in dic and dic[v]:
                    res = min(res, N - (i + 1 + (N - dic[v][-1])))
            else:
                res = min(res, N - (i + 1))
                if dic[0]:
                    res = min(res, N - (i + 1 + (N - dic[0][-1])))
        
        return res if res < inf else -1