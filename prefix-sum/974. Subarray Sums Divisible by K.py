class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        nums[0] %= k
        for i in range(1, len(nums)):
            nums[i] = (nums[i] + nums[i - 1]) % k
        
        dic = Counter(nums)
        res = 0
        
        for i ,j in dic.items():
            if i == 0:
                res += int((j * (j + 1)) / 2)
            else:
                res += int((j * (j - 1)) / 2) 

        return res