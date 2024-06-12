# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=head
        while node:
            if node.next:
                val=gcd(node.val,node.next.val)
                elem=ListNode(val)
                elem.next=node.next
                node.next=elem
                node=node.next.next
            else:
               node=node.next
        return head