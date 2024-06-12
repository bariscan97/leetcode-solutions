# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node: return 
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
            
        ans = []
        dfs(root)
        tree=TreeNode(ans[0])
        node=tree
        
        for i in ans[1:]:
            node.right=TreeNode(i)
            node=node.right
        return tree