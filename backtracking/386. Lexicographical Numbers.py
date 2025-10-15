class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        def f(num, digit):
            print(num)
            if num > n:
                return
            if num: res.append(num)
            for i in range(0 if digit else 1, 10):
                f(num * 10 + i, digit + 1)

        res = []   
        f(0,0)
        
        return res