class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
     
        
        def is_valid(words):
            arr = []
            for i in words:
                if arr == [] and i == ")":
                    return False
                if arr and i == ")":
                    arr.pop()
                elif i == "(":
                    arr.append(i)
            return arr == []
        
        res = defaultdict(set)
        q = deque()
        q.append([s,0])
        visited = set()
        cnt = 0
        while q:
            words ,cnt = q.popleft()
            
            if cnt - 1 in res:
                return res[cnt - 1]
            if is_valid(words):
                res[cnt].add(words)
               
            else:
                
                    for i in range(len(words)):
                        x = words[:i] + words[i + 1:]
                        
                        flag = False
                        for i in range(len(x)) :
                            if i != ")" and i != "(":
                                flag = True
                                break
                        if (flag or "()" in x) and not x in visited:
                            q.append([x, cnt + 1])
                            visited.add(x)
        
        if len(res) == 0:return [""]
        ans = res[list(res.keys())[0]]
        return ans if ans else [""]