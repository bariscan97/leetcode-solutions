"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        def dfs(node):
            res.append(node.val)
            for i in node.children:
                dfs(i)
        
        res = []
        dfs(root)

        return res
            
        