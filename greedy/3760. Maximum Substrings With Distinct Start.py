class Solution:
    def maxDistinct(self, s: str) -> int:
        curr = s[0]
        seens = set()
        seens.add(curr)
        
        for i in s[1:]:
            if not i in seens:
                curr = i
                seens.add(i)

        return len(seens)