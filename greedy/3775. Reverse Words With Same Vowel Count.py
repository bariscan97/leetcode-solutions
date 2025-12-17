vowels = set("aeiou")

def vowelsCnt(s):
    cnt = 0
    for i in s:
        if i in vowels:
            cnt += 1
    return cnt

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        firstVowelCnt = vowelsCnt(s[0])

        for i in range(1, len(s)):
            if vowelsCnt(s[i]) == firstVowelCnt:
                s[i] = s[i][::-1]
        
        return " ".join(s)