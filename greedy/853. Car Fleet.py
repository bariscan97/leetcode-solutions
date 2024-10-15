class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        arr=sorted([[pos[i],speed[i]] for i in range(len(pos))],reverse=True)
        point, res = arr[0] , 1
        for i in range(1,len(arr)):
            if (target - point[0]) / point[1] < (target - arr[i][0]) / arr[i][1]:
                res += 1
                point = arr[i]
        return res