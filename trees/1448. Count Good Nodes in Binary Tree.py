# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        val = root.val
        
        def dfs(node,max_val):
            nonlocal res
            if node is None:
                return 
            if max_val <= node.val:
                res += 1
            dfs(node.left,max(max_val,node.val))
            dfs(node.right,max(max_val,node.val))
        dfs(root,val)
        
        return res