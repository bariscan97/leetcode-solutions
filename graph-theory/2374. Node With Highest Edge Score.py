class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = [0 for i in range(len(edges))]
        for i in range(len(edges)):
            scores[edges[i]] += i
        
        res = [-1, -1]
        for i in range(len(scores) - 1, -1 , -1):
            if scores[i]  >= res[1]:
                res = [i, scores[i]] 
       
        return res[0]