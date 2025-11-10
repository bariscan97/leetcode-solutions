class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        def f(A):
            res = 0
            stack = []
            for i in A:
                
                while stack and stack[-1] > i:
                    val = stack.pop()
                    res += 1
                
                if not stack or stack[-1] != i:
                    stack.append(i)
            
            return res + len(stack)
        
        arr = []
        ans = 0
        
        for num in nums:
            if num:
               arr.append(num)
            else:
                ans += f(arr)
                arr = []
        
        return ans + f(arr)