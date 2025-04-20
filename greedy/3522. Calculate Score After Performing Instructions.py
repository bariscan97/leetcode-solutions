class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        res = i = 0
        N = len(instructions)
        visited = set()
        visited.add(i)
        while -1 < i <  N:
            if instructions[i] == "add":
                res += values[i]
                i += 1
            else:
                i += values[i]
            if i in visited:
                break
            visited.add(i)
        return res