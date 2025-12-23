class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        events.sort()
        suffix = [0] * N
        suffix[-1] = events[-1][-1]
        
        for i in range(N - 2, -1, -1):
            suffix[i] = max(events[i][-1], suffix[i + 1])

        res = max(suffix)

        for i in range(N):
            start, end, val = events[i]
            idx = bisect_left(events,[end + 1, -1, -1])
            if idx < N:
                res = max(res, suffix[idx] + val)
    
        return res