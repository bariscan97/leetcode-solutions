class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        sl = SortedList([[0,i] for i in range(n)])
        dic = Counter()

        for start, end in meetings:
            
            diff = end - start
            idx = 0
            mini = [0, sl[0][1], sl[0][0]]
            
            while idx < n:
                e, r = sl[idx]
                if e > start:
                    break
                if r < mini[1]:
                    mini = [idx, r, e] 
                idx += 1
            
            idx , room, e  = mini
            del sl[idx]  
            sl.add([max(e, start) + diff, room])
            dic[room] += 1
           
        return sorted(
            [[i,j] for i, j in dic.items()], 
            key = lambda x:[-x[1],x[0]]
        )[0][0]