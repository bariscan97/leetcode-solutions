class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        q = deque()
        q.append(["0000" ,0])
        visited = set()
        while q:
            curr ,cnt = q.popleft()
            if curr  == target:
                return cnt
            if curr in deadends or curr in visited:
                continue
            visited.add(curr)
            for j in range(4):
                q.append([curr[:j] + str((int(curr[j]) + 1) % 10) + curr[j + 1:], cnt + 1])
                q.append([curr[:j] + str((int(curr[j]) - 1) % 10) + curr[j + 1:], cnt + 1])
        
        return -1