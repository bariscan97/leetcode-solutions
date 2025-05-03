class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        counts = Counter()
        dominos = {i : [0, 0] for i in range(1, 7)}
        for i, j in zip(tops, bottoms):
            if i == j :
                counts[i] += 1
            else:
                counts[i] += 1
                counts[j] += 1
                dominos[i][0] += 1
                dominos[j][1] += 1
        res = inf
        for i, j in dominos.items():
            if counts[i] == len(bottoms):
                res = min(res, min(j))
        return res if res < inf else -1