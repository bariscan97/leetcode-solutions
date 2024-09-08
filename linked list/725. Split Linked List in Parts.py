# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        arr = list()
        res = [[] for i in range(k)]
        while head:
            arr.append(head.val)
            head = head.next
        start = 0
        rem = len(arr) % k
        div = len(arr) // k
        print(rem, div)
        for i in range(len(arr)):
            res[start].append(arr[i])
            if rem:
                if len(res[start]) == div + 1:
                    start += 1
                    rem -= 1
            else:
                if len(res[start]) == div:
                    start += 1
     
        for i in range(len(res)):
            head = ListNode(res[i][0] if res[i] else "")
            node = head
            for link in res[i][1:]:
                node.next = ListNode(link)
                node = node.next
            res[i] = head
    
        return res
