def parse(s):
    res = []
    curr = ""
    for i in s:
        if not i in ["+","-","*"]:
           curr += i
        else:
            res.append(int(curr))
            res.append(i)
            curr = ""
  
    return res + [int(curr)]

def calc(arr):
    v = []
    flag = 1
    op = False
    for i in arr:
        if i in ["+","-","*"]:
            op = False
            match i:
                case "+": flag = 1      
                case "-": flag = -1
                case "*":
                    op = True
                    total = sum(v[:-1])
                    v = [total, v[-1]]
        else:
            if op:
                v[-1] *= i
            else:
                v.append(flag * i)
    
    return sum(v)

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
    
        res = []
        
        def f(i, s, l_idx):
            
            if i == len(num):
                if calc(parse(s)) == target:
                    res.append(s)
                return 
            f(i + 1, s + f"+{num[i]}", len(s))
            f(i + 1, s + f"-{num[i]}", len(s))
            f(i + 1, s + f"*{num[i]}", len(s))
            if (l_idx is None and s[0] != "0") or (l_idx and s[l_idx + 1] != "0"):
               f(i + 1, s + num[i], l_idx)
        
        f(1, num[0], None)
        
        return res