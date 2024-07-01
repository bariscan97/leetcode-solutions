class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dic = {1 : deque()}
        res = -1
        for i in range(len(seats)):
            if seats[i] == 1:
                dic[1].append(i)
        last_idx = None
        for i in range(len(seats)):
            if seats[i] == 1:
                last_idx = i
                dic[1].popleft()
            else:
                val = None
                if dic[1] :
                    val = dic[1][0]
                if val != None:
                    if last_idx != None:
                        res = max(res, min(abs(i - val), abs(i - last_idx)))
                    else:
                        res = max(res, abs(i - val))
                else:
                    res = max(res ,abs(i - last_idx))
        return res