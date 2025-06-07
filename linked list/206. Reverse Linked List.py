# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
        
        _head = ListNode(arr[-1])        
        node = _head

        for i in arr[::-1][1:]:
            node.next = ListNode(i)
            node = node.next

        return _head