# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = [-inf, inf]
        depth = 0
        q = deque()
        q.append(root)

        while q:
            total = 0
            for _ in range(len(q)):
                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            depth += 1

            if (total > res[0]) or (res[0] == total and res[1] > depth):
                res = [total, depth]
        

        return res[1]