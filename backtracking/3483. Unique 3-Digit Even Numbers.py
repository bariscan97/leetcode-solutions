class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        
        def f(val):
            if 99 < val < 1000:
                print(val) 
                if val % 2:
                    return 0
                return 1
            seens = set()
            res = 0
            for i in range(len(digits)):
                if not val and not digits[i]:
                    continue
                if not i in visited and not digits[i] in seens:
                    visited.add(i)
                    seens.add(digits[i])
                    res += f(val * 10 + digits[i])
                    visited.remove(i)
            return res
        visited = set()
        return f(0)