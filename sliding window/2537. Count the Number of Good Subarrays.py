class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        res = 0
        j = 0
        dic = Counter()
        total = 0
        for i in range(len(nums)):
            if dic[nums[i]] > 1:
                total -= int(((dic[nums[i]] - 1) * dic[nums[i]]) / 2)
            dic[nums[i]] += 1
            if dic[nums[i]] > 1:
                total += int(((dic[nums[i]] - 1) * dic[nums[i]]) / 2)
   
            while total >= k:
                if dic[nums[j]] > 1:
                    total -= int(((dic[nums[j]] - 1) * dic[nums[j]]) / 2)
                dic[nums[j]] -= 1
                if dic[nums[j]] > 1:
                    total += int(((dic[nums[j]] - 1) * dic[nums[j]]) / 2)
                j += 1
            res += j
        
        return res