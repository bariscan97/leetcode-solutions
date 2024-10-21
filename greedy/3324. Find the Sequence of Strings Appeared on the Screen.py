class Solution:
    def stringSequence(self, target: str) -> List[str]:
        string = ""
        idx = 0
        res = []
        while string != target:
            val = "a"
            while val != target[idx]:
                res.append(string + val)
                val = chr(ord(val) + 1)
            idx += 1
            string += val
            res.append(string)
        return res