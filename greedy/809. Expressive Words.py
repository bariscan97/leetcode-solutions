def parse(s):
    slc = []
    prev = s[0]
    cnt = 1
    for curr in s[1:]:
        if curr == prev:
            cnt += 1
        else:
            slc.append([prev, cnt])
            cnt = 1
        prev = curr
    slc += [[prev, cnt]]
    return slc

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        parsed_s = parse(s)
        res = 0
        for word in words:
            flag = True
            parsed_word = parse(word)
            if len(parsed_s) == len(parsed_word):
                for i, j in zip(parsed_s, parsed_word):
                    if (
                        i[0] != j[0] or
                        i[1] < j[1] or
                        (i[1] == 2 and j[1] == 1)
                    ):
                        flag = False
                        break
                if flag:
                    res += 1
           
        return res