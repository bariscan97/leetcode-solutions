class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        return sorted([i for i, j in Counter(bulbs).items() if j % 2])