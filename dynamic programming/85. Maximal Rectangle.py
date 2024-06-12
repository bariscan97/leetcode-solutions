class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        m , n = len(matrix) , len(matrix[0])
        res = 0
        
        for j in range(n):
            cnt = 1
            for i in range(m - 1,- 1 , -1):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0
                    cnt = 1
                else:
                    matrix[i][j] = cnt
                    cnt += 1
        
        for i in matrix:
            val = None
            cnt = 1
            stack = []
            for j in i:
                if j == 0:
                    val = None
                    cnt = 1
                    stack = []
                    continue
                idx = cnt
                while stack and stack[-1][0] > j:
                    val , idx = stack.pop()
                    res = max(res , val * (cnt - idx))
                stack.append([j,idx])     
                for elem in stack:
                    res = max(res , ((cnt + 1) - elem[1]) * elem[0])    
                cnt += 1

        return res