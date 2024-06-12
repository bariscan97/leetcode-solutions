class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        def dfs(q,arr,sub,ind):
            nonlocal res
            if sub:
                if not (self.backtrack(ind[0],ind[1],sub,ind,"left") and self.backtrack(ind[0],ind[1],sub,ind,"right")):
                    return
                
            if len(sub)==n:
                res+=1
                return     
                
            for i in range(len(arr)):
                
                dfs(q,arr[:i]+arr[i+1:],sub+[q[:arr[i]]+["Q"]+q[arr[i]+1:]],[len(sub),arr[i]])

        dfs(["." for i in range(n)],[i for i in range(n)],[],[None,None])
        
        return res
    def backtrack(self,x,y,subCheck,start,rot):
        
            if x == -1 or y  == -1 or x==len(subCheck) or y == len(subCheck[0]):
                return True
            if subCheck[x][y]=="Q" and start!=[x,y]:
                    return False
            if rot == "left":
                return self.backtrack(x-1,y+1,subCheck,start,rot)
            else:
                return self.backtrack(x-1,y-1,subCheck,start,rot)
       
        









            