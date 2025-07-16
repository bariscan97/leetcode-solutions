class StreamChecker:

    def __init__(self, words: List[str]):
        
        self.trie = {}
        self.s = ""
        
        for word in words:
            curr = self.trie
            for i in word[::-1]:
                if not i in curr:
                    curr[i] = {}
                curr = curr[i]
            curr["ok"] = True
        
    def query(self, letter: str) -> bool:
        
        self.s += letter
        curr = self.trie
        
        for i in range(len(self.s) - 1, -1 ,-1):
            if not self.s[i] in curr:
                break
            curr = curr[self.s[i]]
            if "ok" in curr:
                return True
        
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)