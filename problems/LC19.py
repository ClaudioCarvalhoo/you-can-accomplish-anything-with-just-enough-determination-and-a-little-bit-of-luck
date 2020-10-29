# O(n)
# n = depth(head)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current = head
        scout = head

        for i in range(n):
            if scout.next != None:
                scout = scout.next
            else:
                return current.next

        while True:
            if scout.next == None:
                current.next = current.next.next
                break
            else:
                scout = scout.next
                current = current.next

        return head