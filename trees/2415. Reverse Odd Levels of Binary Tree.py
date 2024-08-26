# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node, cnt):
            if node is None:
                return
            dfs(node.left, cnt + 1)
            dfs(node.right, cnt + 1)
            if cnt % 2:
                stacks[cnt].append(node.val)
      
        stacks = defaultdict(list)
        dfs(root ,0)

        q = deque()
        q.append([0 , root])  

        while q:
            cnt ,node = q.popleft()
            if node is None:
                continue
            if cnt % 2:
                node.val = stacks[cnt].pop()
            q.append([cnt + 1, node.left])
            q.append([cnt + 1, node.right])

        return root