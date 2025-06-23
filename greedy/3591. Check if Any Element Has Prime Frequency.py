def is_prime(n: int) -> bool:
    if n < 2:            
        return False
    limit = math.isqrt(n)        
    for d in range(2, limit + 1, 1):   
        if n % d == 0:
            return False
    return True

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        
        for i in Counter(nums).values():
            if is_prime(i):
                return True
        return False