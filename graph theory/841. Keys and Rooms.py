class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        visited = set()
        q = deque()
        q.append(0)
        
        while q:
            idx = q.popleft()
            if idx in visited:
                continue
            
            visited.add(idx)

            for key in rooms[idx]:  
                q.append(key)
        
        return len(visited) == N
            