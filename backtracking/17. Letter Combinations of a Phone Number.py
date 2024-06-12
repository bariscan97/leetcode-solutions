class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":return []
        dic={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        res=set()
        size=len(digits)
        def helper(str1,text):
            nonlocal size
            if len(str1)==size:
                res.add(str1)
                return 
            for i in text:
                for j in dic[int(i)]:
                    helper(str1+j,text[1:])
                text=text[1:]
        helper("",digits)
        return res 