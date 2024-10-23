# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels_sum = Counter()
        color = 0
        pairs = Counter()
        def dfs1(node, parent ,level):
            nonlocal color
            if node is None:
                return
            color += 1
            if node.left and parent:
                pairs[parent] += node.left.val
            if node.right and parent:
                pairs[parent] += node.right.val
            dfs1(node.left, color, level + 1)
            dfs1(node.right, color, level + 1)
            levels_sum[level] += node.val
        
        def dfs2(node, parent ,level):
            nonlocal color
            if node is None:
                return
            color += 1
            if node.left and (parent != None or (parent and parent > 1)):
                if levels_sum[level + 1]:
                    node.left.val = levels_sum[level + 1] - pairs[parent]
            if node.right and (parent != None or (parent and parent > 1)):
                if levels_sum[level + 1]:
                    node.right.val = levels_sum[level + 1] - pairs[parent]
            if level <= 1:
                node.val = 0
            dfs2(node.left, color, level + 1)
            dfs2(node.right, color, level + 1)
            
        dfs1(root, None, 0)
        color = 0
        dfs2(root, None, 0)
       
        return root