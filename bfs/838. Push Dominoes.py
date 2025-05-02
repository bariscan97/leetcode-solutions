class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        N = len(dominoes)
        q = deque()
        for i in range(N):
            if dominoes[i] != ".":
                q.append(i)
        while q:
            visited = set()
            for _ in range(len(q)):
                idx = q.popleft()
                match dominoes[idx]:
                    case "R":
                        if -1 < idx + 1 < N:
                            if idx + 1 in visited:
                                dominoes[idx + 1] = "."
                                continue
                            if dominoes[idx + 1] == ".":
                                dominoes[idx + 1] = "R"
                                visited.add(idx + 1)
                                q.append(idx + 1)
                    case "L":
                        if -1 < idx - 1 < N:
                            if idx - 1 in visited:
                                dominoes[idx - 1] = "."
                                continue
                            if dominoes[idx - 1] == ".":
                                dominoes[idx - 1] = "L"
                                visited.add(idx - 1)
                                q.append(idx - 1)
       
        return "".join(dominoes)