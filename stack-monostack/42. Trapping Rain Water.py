class Solution:
    def trap(self, arr: List[int]) -> int:
        
        res ,stack = 0 , []
        
        for i in range(len(arr)):
            
            last_idx = i
            val  = arr[i]
          
            while stack and arr[stack[-1]] < arr[i]:
            
                val = min(arr[stack[0]],arr[i])
                idx = stack.pop()
                res += (val - arr[idx]) * (last_idx - idx)
                last_idx = idx
            
            arr[last_idx] = arr[i]
            stack.append(last_idx)
        
        return res