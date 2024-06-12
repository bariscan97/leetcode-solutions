class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack=[-1]
        ans=[]
        for i in prices[::-1]:
            while i<stack[-1]:
                stack.pop()
            ans.append(stack[-1])
            stack.append(i)
        print(ans)
        ans=ans[::-1]
        for i in range(len(prices)):
            if ans[i]!=-1:
                prices[i]-=ans[i]
        return prices