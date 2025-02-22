# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        space_cnt = 0
        num = ""
        arr, stack = [], []
        flags = [True, False]
        for i in traversal:
            if i == "-":
                if flags[0] and flags[1]:
                    arr.append([space_cnt,num])
                    flags[1] = False
                    num = ""
                    space_cnt = 0
                flags[0] = True
                space_cnt += 1
            else:
                num += i
                flags[1] = True
        arr.append([space_cnt,num])
        
        for cnt, num in arr:
            
            while stack and stack[-1][0] >= cnt:
                stack.pop()
            
            node = TreeNode(int(num))
            if stack:
                if stack[-1][1].left is None:
                    stack[-1][1].left = node
                else:
                    stack[-1][1].right = node
            stack.append([cnt, node])
     
        return stack[0][1]