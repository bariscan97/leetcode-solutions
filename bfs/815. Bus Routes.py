class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        dic = defaultdict(list)
        for i in range(len(routes)):
            for j in routes[i]:
                dic[j].append(i)
        q = deque()
        q.append([0,source])
        visited = set()
        visited.add(source)
        while q:
            cnt ,curr = q.popleft()
            if curr == target:
                return cnt
            for paths in dic[curr]:
                if not ("path",paths) in visited:
                    visited.add(("path",paths))
                    for path in routes[paths]:
                        if not path in visited:
                            visited.add(path)
                            q.append([cnt +  1,path])
        return -1