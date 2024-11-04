class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        cnt = 1
        curr = word[0]
        for i in word[1:]:
            if i == curr:
                cnt += 1
            else:
                x = cnt // 9
                div = cnt % 9
                if cnt <= 9:
                    res += f"{cnt}{curr}"
                else:
                    res += f"{9}{curr}" * x 
                    if div != 0:
                        res += f"{div}{curr}"
                curr = i
                cnt = 1
        x = cnt // 9
        div = cnt % 9
        if cnt <= 9:
            res += f"{cnt}{curr}"
        else:
            res += f"{9}{curr}" * x
            if div != 0:
                res += f"{div}{curr}"
        return res