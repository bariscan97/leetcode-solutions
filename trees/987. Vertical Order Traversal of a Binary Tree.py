# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def dfs(node,val,depth):
            if node is None:return
            if val in dic:
                if depth in dic[val]:
                    heappush(dic[val][depth],node.val)
                else:
                    dic[val][depth] = []
                    heappush(dic[val][depth],node.val)
            else:
                dic[val] = {depth:[]}
                heappush(dic[val][depth],node.val)
            dfs(node.left,val-1,depth+1)
            dfs(node.right,val+1,depth+1)
        dic = dict()
        dfs(root,0,0)
        res = []
        for i in sorted(dic.keys()):
            arr = []
            for j in sorted(dic[i].keys()):
                while dic[i][j]:
                    arr.append(heappop(dic[i][j]))
            res.append(arr)
        return res