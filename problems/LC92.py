# O(n)
# n = len(head)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        preHead = ListNode(None, head)
        node = preHead
        pos = 0
        while pos < left - 1:
            node = node.next
            pos += 1
        preReversal = node

        prev = preReversal
        node = node.next
        pos += 1
        while pos <= right:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
            pos += 1
        preReversal.next.next = node
        preReversal.next = prev

        return preHead.next
