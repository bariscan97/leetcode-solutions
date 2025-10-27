class Solution:
    def removeZeros(self, n: int) -> int:
        res = 0
        digit = 1
        while n:
            num = n % 10
            if num:
                res += digit * num
                digit *= 10
            n //= 10
        return res