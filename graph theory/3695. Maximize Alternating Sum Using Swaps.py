class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return 

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        N = len(nums)
        uf = UnionFind(N)
        
        for i, j in swaps:
            uf.union(i,j)
    
        dic = {}
        res = 0

        for i in range(N):
            parent = uf.find(i)
            if not parent in dic:
                dic[parent] = [0, []]
            if not i % 2:
                dic[parent][0] += 1 
            heappush(dic[parent][1], -nums[i])

        for k, v in dic.items():
            while v[1]:
                val = heappop(v[1])
                if v[0] < 1:
                    res += val
                else:
                    res -= val
                v[0] -= 1

        return res