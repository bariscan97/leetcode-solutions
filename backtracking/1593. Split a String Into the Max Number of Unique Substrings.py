class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def f(i, string):
            if i == len(s):
                return 0
            val = 0
            if not string + s[i] in visited:
                visited.add(string + s[i])
                val = max(val ,f(i + 1, "") + 1)
                visited.remove(string + s[i])
            return max(val, f(i + 1, string + s[i]))
        visited = set()
        return f(0, "") 