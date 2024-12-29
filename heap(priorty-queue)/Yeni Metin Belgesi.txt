class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        _heap = [[-ord(i), j] for i, j in Counter(s).items()]
        heapify(_heap)
        quantity = 0
        res = ""
       
        while _heap:
            char, cnt = heappop(_heap)
            if res and ord(res[-1]) * -1 == char:
                if quantity == repeatLimit:
                    if _heap:
                        char2, cnt2 = heappop(_heap)
                        res += chr(char2 * -1)
                        quantity = 0
                        if cnt2 > 1:
                            heappush(_heap, [char2, cnt2 - 1])
                    else:
                        break
                quantity += 1
            else:
                quantity = 1
            res += chr(char * -1)
            if cnt > 1:
                heappush(_heap, [char, cnt - 1])
       
        return res