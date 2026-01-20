# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        
        while head:
            curr = ListNode(head.val)
            while stack and stack[-1].val < curr.val:
                stack.pop()
            if stack:
                stack[-1].next = curr
            stack.append(curr)
            head = head.next
        
        return stack[0]