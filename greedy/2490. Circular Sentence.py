class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        flag = False
        curr = sentence[0]
        for i in sentence[1:]:
            if i == " ":
                flag = True
                continue
            if flag:
                if i != curr:
                    return False
            flag = False
            curr = i
        return sentence[0] == sentence[-1] 