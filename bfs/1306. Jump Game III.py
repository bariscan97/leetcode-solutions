class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        N = len(arr)
        q = deque()
        q.append(start)
        visited = set()
        while q:
            idx = q.popleft()
            if not arr[idx]:
                return True
            visited.add(idx)
            left = idx - arr[idx]
            right = arr[idx] + idx
            if right < N and not right in visited:
                q.append(right) 
            if left > -1 and not left in visited:
                q.append(left)
        return False