from sortedcontainers import SortedList
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr=SortedList()
        for i in lists:
            head = i
            while head:
                arr.add(head.val)
                head=head.next
        if arr==[]:return
        head_=ListNode(arr[0])
        node=head_
        for i in arr[1:]:
            node.next=ListNode(i)
            node=node.next
        return head_