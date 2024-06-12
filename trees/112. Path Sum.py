# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node,total):
            if node is None:
                return 
            left = dfs(node.left ,total - node.val)
            right = dfs(node.right ,total - node.val)
            if node.left == node.right == None:
                if total == node.val:
                    return True
                return False
            return left or right
        return dfs(root,targetSum)