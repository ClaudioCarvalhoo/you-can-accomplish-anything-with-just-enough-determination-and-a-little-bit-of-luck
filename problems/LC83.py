# O(n)
# n = len(head)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        while node is not None:
            while node.next is not None and node.next.val == node.val:
                node.next = node.next.next
            node = node.next
        return head