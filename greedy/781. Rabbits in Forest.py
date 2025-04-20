class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        for i, j in Counter(answers).items():
            res += i + 1 if j % (i + 1) else 0
            res += ((i + 1) * (j // (i + 1)))
        return res