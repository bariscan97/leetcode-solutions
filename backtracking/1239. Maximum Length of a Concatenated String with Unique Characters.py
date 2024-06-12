class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def dfs(ind,dic):
            nonlocal res   
            res = max(res,len(dic))
            
            for i in range(ind,len(arr)):
                go = True
                
                for j in arr[i]:
                    if j in dic:
                        go = False
                        break
                   
                if go and len(arr[i]) == len(set(arr[i])):
                    dfs(i+1,dic+arr[i])
                else:
                    dfs(i+1,dic)
        res = 0
        dfs(0,"")
        
       
        return res