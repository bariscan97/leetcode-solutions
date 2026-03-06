class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = [nums[0]]
        
        for i in nums[1:]:
            if stack[-1] == i:
                stack[-1] += i
                idx = len(stack) - 2
                while idx > -1:
                    if stack[idx] == stack[-1]:
                        stack[idx] += stack[-1]
                        stack.pop()
                    else:
                        break
                    idx -= 1
            else:
                stack.append(i)
            
        return stack
