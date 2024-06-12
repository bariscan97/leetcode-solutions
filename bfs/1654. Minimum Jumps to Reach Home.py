class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        upper = max(forbidden | {x}) + a + b
        
        ans = 0
        queue = [(0, 0)]
        forbidden.add(0)
        while queue: 
            newq = []
            for n, k in queue: 
                if n == x: return ans
                if n+a <= upper and n+a not in forbidden: 
                    newq.append((n+a, 0))
                    forbidden.add(n+a)
                if k == 0 and 0 <= n-b and n-b not in forbidden: 
                    newq.append((n-b, 1))
            ans += 1
            queue = newq
        return -1 