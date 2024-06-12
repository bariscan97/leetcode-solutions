# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:return True
        res=True
        def dfs(node):
            nonlocal res
            if node is None:
               return 0
            l=dfs(node.left)
            r=dfs(node.right)    
            if abs(l-r)>1:
                res=False
            return 1+max(l,r)
        dfs(root)
        return res

           