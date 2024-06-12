class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(i,arr):
            nonlocal res
            if len(arr) == k:
                res.append(arr)
                return 
            for idx in range(i + 1,n + 1):
               backtrack(idx , arr + [idx])
        res = []
        for i in range(1, n + 1):
            backtrack(i,[i])
        return res