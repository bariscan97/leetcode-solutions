class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=set()
        def helper(candidates,sub,target):
            if target==0:
                res.add(tuple(sorted(sub)))
            if target<=0:return
            for i in range(len(candidates)):
                helper(candidates,sub+[candidates[i]],target-candidates[i])
        helper(candidates,[],target)
        
        return res