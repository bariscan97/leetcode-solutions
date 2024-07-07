class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        def f(string):
            if len(string) == n:
                res.append(string)
                return
            for i in  ["0" , "1"]:
                if (i == "0" and string and string[-1] != "0") or len(string) == 0 or i == "1":
                    f(string + i)
        res = []
        f("")   
        return res