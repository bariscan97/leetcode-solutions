class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        vals = [[-j, i] for i ,j in Counter(tasks).items()]
        heapify(vals)
        res = 0
        while True:
            q = deque()
            while vals:
                if len(q) - 1 == n:
                    break
                q.append(heappop(vals))
            res += len(q)
            size = len(q)
            for i in range(len(q)):
                val = q.popleft()
                val[0] *= - 1
                if val[0] > 1:
                    heappush(vals, [-1 * (val[0] - 1), val[1]])
            if len(vals) == 0:
                break  
            res +=  max(0,n - (size - 1))
        return res