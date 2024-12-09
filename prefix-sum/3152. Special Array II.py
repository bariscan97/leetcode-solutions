class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        size = len(nums)
        prefix = [[0,0] for i in range(size)]
        val = 0
        for i in range(size - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                val += 1
            prefix[i][1] = val
            prefix[i + 1][0] = val
        res = []
        for start ,end in queries:
            res.append(prefix[start][0] == prefix[end][0]) 
        return res