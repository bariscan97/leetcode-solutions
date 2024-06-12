class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        
        res = 0
        stack = []
        for i in range(len(arr)):
            idx = i
            while stack and stack[-1][0] > arr[i]:
                val , idx = stack.pop()
                res = max(res , val * (i - idx))
            stack.append([arr[i],idx])
            
        for i in stack:
            res = max(res , (len(arr) - i[1]) * i[0])
      
        return res