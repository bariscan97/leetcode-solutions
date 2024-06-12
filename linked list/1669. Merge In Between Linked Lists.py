# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        node1 = list1
        node2  = list1
        list2_node = list2
        while list2_node.next:
            list2_node = list2_node.next
        cnt = 0 
        while node2:
            if cnt < a - 1:
                node1 = node1.next
            node2 = node2.next
            if cnt == b:
                list2_node.next = node2
                node1.next = list2
                return list1
            cnt += 1