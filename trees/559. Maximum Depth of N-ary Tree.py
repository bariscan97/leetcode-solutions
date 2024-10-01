"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        def dfs(node, cnt): 
            nonlocal res
            res = max(res, cnt)
            for i in node.children:
                dfs(i, cnt + 1)
        
        res = 0
        dfs(root, 0)

        return res + 1