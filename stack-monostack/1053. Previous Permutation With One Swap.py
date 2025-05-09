class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        stack = []
        for i in range(len(arr) -1, -1, -1):
            if stack:
                if stack[-1][0] > arr[i]:
                    stack.append([arr[i], i])
                elif stack[-1][0] == arr[i]:
                    stack[-1][1] = i
                else:
                    prev = None
                    while stack:
                        if stack[-1][0] < arr[i]:
                            prev = stack.pop()
                        else:
                            break
                    if prev != None:
                        arr[i], arr[prev[1]] = prev[0], arr[i]      
                        break
            else:
                stack.append([arr[i], i])
        return arr