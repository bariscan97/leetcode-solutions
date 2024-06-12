# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        all_sums = []
        def sum_subtree(root):
            if root is None: return 0
            total_sum = root.val + sum_subtree(root.left) + sum_subtree(root.right)
            all_sums.append(total_sum)
            return total_sum
        
        total = sum_subtree(root)
        res = 0
        for s in all_sums:
            res = max(res, s*(total-s))
        return res % (10**9+7)
        