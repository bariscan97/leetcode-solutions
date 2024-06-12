class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for i in range(len(spells)):
            val  = success / spells[i]
            idx = bisect_left(potions,val)
            res.append(len(potions) - idx)
        return res 