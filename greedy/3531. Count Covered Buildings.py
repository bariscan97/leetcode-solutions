class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x , y = {} , {}
        res = 0
        
        for i, j in buildings:
            if not i in x:
                x[i] = [n + 1, -1]
            if not j in y:
                y[j] = [n + 1, -1]
            x[i] = [min(x[i][0], j), max(x[i][1], j)]
            y[j] = [min(y[j][0], i), max(y[j][1], i)]
        
        for i, j in buildings:
            if x[i][0] < j < x[i][1] and y[j][0] < i < y[j][1]:
                res += 1
        
        return res