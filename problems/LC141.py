# O(n)
# n = len(head)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        p1 = head
        p2 = head.next
        while p2 is not None:
            if p1 == p2:
                return True
            p1 = p1.next
            p2 = p2.next
            if p2 is not None:
                p2 = p2.next
        return False