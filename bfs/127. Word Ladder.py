class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        q.append([beginWord,1])
        visited = set()
        wordList = set(wordList)
        while q:
            word, cnt = q.popleft()
            if word in visited:
                continue
            if word == endWord:
                return cnt
            visited.add(word)
            for i in range(len(word)):
                for char in ascii_lowercase:
                    new = word[:i] + char + word[i + 1:]
                    if new in wordList:
                        q.append([new, cnt + 1])
        return 0    