class Solution:
    def calculate(self, s: str) -> int:
        curr = ""
        arr = []
        
        for i in s:
            if i == " ":
                continue
            if "0" <= i <= "9":
                curr += i
            else:
                arr.append(curr)
                arr.append(i)
                curr = ""
        
        arr.append(curr)
        stack = []
       
        for i in arr:
            val = i
            if not i in ["*","-","/","+"] and stack:
                if stack[-1] in ["*","/"]:
                    op = stack.pop()
                    num = stack.pop()
                    match op:
                        case "*":
                            val = str(floor(float(i) * float(num)))
                        case "/":
                            val = str(floor(float(num) / float(i)))  
                    
            stack.append(val)
            
        res = [float(stack[0])]
        c = None
        
        for i in stack[1:]:
            if i in ["*","-","/","+"]:
                c = i
            else:
                if c == "+":
                    res.append(float(i))
                else:
                    res.append(-float(i))

            
        return int(sum(res))