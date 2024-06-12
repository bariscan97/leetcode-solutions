# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(node,total):
            nonlocal res
            if node is None:
                return  
            prefix[total] += 1
            if (total + node.val) - targetSum in prefix:
                res += prefix[(total + node.val) - targetSum]
            dfs(node.left ,total + node.val)
            dfs(node.right , total + node.val)
            prefix[total] -= 1
        
        prefix = Counter()
        res = 0
        dfs(root,0)
        return res