class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dic = Counter(words)
        res = 0
        for word in words:
            if word[0] != word[1]:
                if word in dic and word[::-1] in dic:
                    res += min(dic[word], dic[word[::-1]]) * 2
            else:
                if not dic[word] % 2:
                    res += dic[word]
                else:
                    res += dic[word] -1 if res % 2 else dic[word]
            del dic[word]
        return res * 2