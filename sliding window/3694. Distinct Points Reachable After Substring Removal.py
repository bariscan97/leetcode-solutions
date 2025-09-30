def f(v, pos, flag = 1):
    match v:
        case "U":
            pos[1] += flag
        case "D":
            pos[1] -= flag
        case "L":
            pos[0] -= flag
        case "R":
            pos[0] += flag

class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        pos = [0,0]
        seens = set()
        
        N = len(s)

        for i in s:
           f(i, pos)
            
        for i in range(N):
            f(s[i], pos, -1)
            if i >= k - 1:
                seens.add(tuple(pos))
                cnt = 0
                f(s[i - (k - 1)], pos)
            
        return len(seens)