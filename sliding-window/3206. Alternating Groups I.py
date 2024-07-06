class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        l ,m ,r = -1 ,0 ,1
        res = 0
        for _ in range(len(colors)):
            if colors[l] != colors[m] and colors[m] != colors[r]:
                res += 1
            l = (1 + l) % len(colors)
            m = (1 + m) % len(colors)
            r = (1 + r) % len(colors)
        return res