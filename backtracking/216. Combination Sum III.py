class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        max_size=(n-k)+1
        res=[]
        def helper(ind,sub,tot):
            nonlocal max_size,k,n
            if len(sub)==k and tot==n:
                res.append(sub)
                return
            if len(sub)==k:
                return 
            for i in range(ind,10):
                helper(i+1,sub+[i],tot+i)
        helper(1,[],0)
        return res