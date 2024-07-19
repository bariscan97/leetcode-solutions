class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        def backtracking(arr ,cnt):
            nonlocal res
            res += 1
            if cnt == 0:
                return
            for i in range(10):
                if not i in arr:
                    if (arr and arr[0] != 0) or not len(arr) :
                        backtracking(arr + [i] ,cnt - 1)
        res = 0
        backtracking([],n)
        return res - 1 if n > 0 else res 
       