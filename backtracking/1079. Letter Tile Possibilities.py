class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res=set()
        size=len(tiles)
        def dfs(tiles,s,cnt):
            if s:
                res.add(s)
            if not tiles:return 
            for i in range(len(tiles)):
                dfs(tiles[:i]+tiles[i+1:],s+tiles[i],cnt+1)
            
            # tiles=tiles[cnt:]
            
        dfs(tiles,"",0)
        # print(res)
        return len(res)
            