class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        prev = nums[0]
        color = 0
        flag = None
        for num in nums[1:]:
            if prev == num:
                return False
            if num > prev:
                if not color % 2 :
                    color += 1
                flag = "inc"
            elif num < prev:
                if color % 2:
                    color += 1
                elif flag != "dec":
                    return False
                flag = "dec"
            
            prev = num
        
        return color == 3