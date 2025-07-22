class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def dfs(curr, left, right):
            if left == right == n:
                res.append(curr)
            if left < n:
                dfs(curr + "(", left + 1, right)
            if left > right:
                dfs(curr + ")", left, right + 1)

        res = []
        dfs("", 0, 0)
        return res