# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        def dfs(node):
            if node is None:
                return ""
            left = dfs(node.left)
            right = dfs(node.right)
            if node.left == node.right == None:
                dic[f"{node.val}"] += 1
                if dic[f"{node.val}"]  == 2:
                    res.append(node)
                return f"{node.val}"
            val = f"{node.val}"
            if node.left:
                val = left + "r" + val
            if node.right:  
                val = val + "l" + right
            dic[val] += 1
            if dic[val] == 2:
                res.append(node)
            return val
        
        dic = defaultdict(int)
        res = list()
        dfs(root)
        return res