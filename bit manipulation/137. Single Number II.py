class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for i in range(32):
            count = 0
            for num in nums:
                if num & (1<<i) == (1<<i): count += 1
            single |= (count%3) << i
            
        return single if single < (1<<31) else single - (1<<32)   