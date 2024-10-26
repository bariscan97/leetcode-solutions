from sortedcontainers import SortedList
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        def dfs(node, level):
            if node is None:
                return 0
            levels[node.val] = level
            left = dfs(node.left, level + 1)
            right = dfs(node.right, level + 1)
            depths[node.val] = max(left, right) 
            if not level in containers:
                containers[level] = SortedList()
            containers[level].add(depths[node.val])
            return depths[node.val] + 1
        levels = Counter()
        depths = Counter()
        containers = dict()
        max_depth = dfs(root, 0)
        res = []
        for query in queries:
            lvl = levels[query]
            depth = depths[query]
            containers[lvl].discard(depth)
            if not containers[lvl]:
                res.append(lvl - 1)
            else:
                res.append(lvl + containers[lvl][-1])
            containers[lvl].add(depth)
      
        return res