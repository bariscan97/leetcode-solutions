class Solution:
    """
    level 0: []
    level 1: [11]                    [22]       [33]
    level 2: [11,22]     [11,33]     [22,33] 
    level 3: [11,22,33]
  
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(res,0,[],nums)
        return res
    def backtracking(self,res,start,subset,nums):
        res.append(list(subset))
        for i in range(start,len(nums)):
           
            self.backtracking(res,i+1,subset+[nums[i]],nums)
            