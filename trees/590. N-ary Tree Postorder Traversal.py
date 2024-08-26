"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        def dfs(node):
            if node is None:
                return
            for i in node.children:
                dfs(i)
            res.append(node.val)
        
        res = []
        dfs(root)
        return res