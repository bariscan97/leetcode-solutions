class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        dic = Counter()
        res = inf
        total = j = 0
        
        for i in range(len(nums)):
            if not dic[nums[i]]:
                total += nums[i]
            dic[nums[i]] += 1
            
            while total >= k:   
                res = min(res, (i - j) + 1)
                dic[nums[j]] -= 1
                if dic[nums[j]] == 0:
                    total -= nums[j]
                j += 1

        return res if res < inf else -1