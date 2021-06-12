# O(n)
# n = len(head)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        preHead = ListNode(None, head)
        node = preHead
        while node is not None:
            while node.next is not None and node.next.val == val:
                node.next = node.next.next
            node = node.next
        return preHead.next