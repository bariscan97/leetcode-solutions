class Solution:
    def combinationSum2(self, cand: List[int], target: int) -> List[List[int]]:
        
        res=[]
        dic = Counter(cand)
        cand = sorted(dic.keys())
        def helper(sub,tot,parent):
           
            if tot==0:
                res.append(sub)
                return 
            for i in cand:
                
                if tot>=i and sub.count(i)<dic[i] and parent<=i:
                    
                    helper(sub+[i],tot-i,i)
                
        helper([],target,0)
        return res