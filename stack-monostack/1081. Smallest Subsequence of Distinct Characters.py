class Solution:
    def smallestSubsequence(self, s: str) -> str:
        dic=Counter(s)
        stack=[]
        res=[]
        for i in range(len(s)):
            while stack and dic[stack[-1]]>0 and s[i]<stack[-1] and not s[i] in stack :
                stack.pop()
            dic[s[i]]-=1
            if not s[i] in stack:stack.append(s[i])
            res.append("".join(stack))
        # print(res)
        return sorted(res,key=lambda x:(x[0],-len(x)))[0]
        # return ""