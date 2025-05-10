class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        curr_idx = res = cnt = 0
        for i in word:
            if vowels[curr_idx] == i:
                cnt += 1
            else:
                idx = vowels.index(i)
                if idx - curr_idx == 1 and cnt:
                    cnt += 1
                    curr_idx += 1
                else:
                    curr_idx = 0
                    cnt = 1 if i == "a" else 0
            if curr_idx == 4:
                res = max(res ,cnt)
        return res