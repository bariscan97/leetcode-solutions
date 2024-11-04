class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = chars[0]
        cnt = 1
        res = ""
        for char in chars[1:]:
            if char != prev:
                res += prev + f"{str(cnt) if cnt > 1 else ''}" 
                cnt = 1
            else:
                cnt += 1
            prev = char
      
        res += prev + f"{str(cnt) if cnt > 1 else ''}"
        
        while chars and res:
            chars.pop()
        for i in res:
            chars.append(i)
        