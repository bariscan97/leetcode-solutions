class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        def f(i, curr):
            if len(curr) > 1:
                res.append(curr)
            seens = set()
            for idx in range(i, len(nums)):
                if nums[idx] in seens:
                    continue
                if not curr or (curr and curr[-1] <= nums[idx]):
                    seens.add(nums[idx])
                    f(idx + 1, curr + [nums[idx]])
                   
        res = []
        f(0, [])
        
        return res