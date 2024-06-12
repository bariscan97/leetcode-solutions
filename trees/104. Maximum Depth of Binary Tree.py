# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res=0
        def dfs(node,depth):
            nonlocal res
            if node is None :return 
            if node.left==node.right==None:
                res=max(res,depth+1)
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,0)
        return res