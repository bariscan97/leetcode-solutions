class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        sames = collections.defaultdict(list)
        added = collections.defaultdict(int)
        for i, num in enumerate(arr):
            sames[num].append(i)
        
        def bfs(start):
            q = deque([(start, 0)])
            seen = set()

            while q:
                c, s = q.popleft()
                if c == n - 1:
                    return s
                
                if c in seen:
                    continue
                seen.add(c)

                if c+1 < n and c+1 not in seen:
                    q.append((c+1, s+1))
                if c-1 >= 0 and c-1 not in seen:
                    q.append((c-1, s+1))
                
                if added[arr[c]] == 0:
                    for i in sames[arr[c]]:
                        if i != c:
                            q.append((i, s+1))
            
                added[arr[c]] = 1
            
        return bfs(0)        