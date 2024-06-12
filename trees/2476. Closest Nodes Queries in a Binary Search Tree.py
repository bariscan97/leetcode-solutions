# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        
        def dfs(node):
        
            if node is None:
                return 
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        arr , res = [] , []
        dfs(root)
        arr.sort()
        for i in queries:
            idx = bisect_left(arr,i)
            if idx == len(arr):
                res.append([arr[-1],-1])
            elif arr[idx] == i:
                res.append([i,i])
            elif arr[idx] > i:
            elif idx == 0:
                    res.append([-1,arr[idx]])
                else:
                    res.append([arr[idx - 1] , arr[idx]])
      
        return res
            

        
        
    
        