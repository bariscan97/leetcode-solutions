class Solution:
    def maxRepOpt1(self, text: str) -> int:
        dic = Counter(text)
        arr = []
        val = None
        cnt = 0
        res = -1
        for i in text:
            if val == i:
                cnt += 1
            else:
                if val != None:
                    arr.append([val,cnt])
                    res = max(res,cnt + 1 if dic[val] > cnt else cnt)
                val = i
                cnt = 1
        arr.append([val,cnt])
        res =  max(res,cnt + 1 if dic[val] > cnt else cnt)
        
        for i in range(1,len(arr) - 1):
            if arr[i - 1][0] == arr[i + 1][0] and arr[i][1] == 1:
                res = max(res,arr[i - 1][1] + arr[i + 1][1] + 1 if arr[i - 1][1] + arr[i + 1][1] < dic[arr[i +1][0]] else arr[i - 1][1] + arr[i + 1][1])
        
        return res