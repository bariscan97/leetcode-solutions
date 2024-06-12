class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        while 1:
            string="".join([str(random.randint(0,1)) for i in range(len(nums))])
            if not string in nums:return string 