class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        N = len(nums)
        grps = []
        nums = sorted([[nums[i],i] for i in range(N)])
        curr = [[nums[0][0]],[nums[0][1]]]
        res = [0] * N
        
        for i in range(1, N):
            if nums[i][0] - curr[0][-1] > limit:
                grps.append(curr)
                curr = [[],[]]
            curr[0].append(nums[i][0])
            heappush(curr[1], nums[i][1])

        for grp in grps+[curr]:
            for i in grp[0]:
                idx = heappop(grp[1])
                res[idx] = i
           
        return res