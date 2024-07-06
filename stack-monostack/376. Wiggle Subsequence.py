class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        stack = [] 
        rot = None
        for i in nums:
            if len(stack) == 0:
                stack.append(i)
            else:
                if rot is None :
                    if len(stack) == 1 and stack[-1] != i:
                        
                        if stack[-1] > i:
                            rot = "d"
                        elif stack[-1] < i:
                            rot = "u"
                        stack.append(i)
                    
                else:
                    if rot == "u" :
                        if stack[-1] > i:
                            stack.append(i)
                            rot = "d"
                        else:
                            stack[-1] = max(stack[-1], i)
                    else:
                        if stack[-1] < i:
                            stack.append(i)
                            rot = "u"
                        else:
                            stack[-1] = min(stack[-1], i)
            
        return len(stack)