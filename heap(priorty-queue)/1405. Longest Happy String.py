class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        _heap = [[-a,"a"],[-b,"b"],[-c,"c"]]
        heapify(_heap)
        curr = None
        res = ""
        while 1:
            
            val ,char = heappop(_heap)
            if val == 0:
                break
            if curr is None:
                res += char
                curr = [1, char]
                heappush(_heap, [val + 1,char])
            elif curr[1] == char and curr[0] >= 2:
                val2 ,char2= heappop(_heap)
                if val2 == 0:
                    break
                res += char2
                curr = [1,char2]
                heappush(_heap,[val2 + 1,char2])
                heappush(_heap, [val ,char])
            elif curr[1] != char:
                res += char
                curr = [1,char]
                heappush(_heap, [val + 1,char])
            else:
                res += char
                curr[0] += 1 
                heappush(_heap, [val + 1,char])
            
        return res