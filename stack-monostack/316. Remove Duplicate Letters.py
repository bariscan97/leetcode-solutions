class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seens = set()
        dic = Counter(s)
        stack = []
        
        for i in s:
            while stack and stack[-1] > i and not i in seens and dic[stack[-1]]:
                val = stack.pop()
                seens.remove(val)
                
            if not i in seens:
                stack.append(i)
            seens.add(i)
            dic[i] -= 1
        
        return "".join(stack)