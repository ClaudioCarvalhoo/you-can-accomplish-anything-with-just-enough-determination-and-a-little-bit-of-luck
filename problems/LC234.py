# O(n) Time | O(1) space
# n = len(head)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        listLen = 0
        node = head
        while node is not None:
            listLen += 1
            node = node.next
        revertUpTo = listLen // 2

        prev = None
        node = head
        for _ in range(revertUpTo):
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        node1 = prev
        node2 = node
        if listLen % 2 != 0:
            node2 = node2.next

        while node1 is not None:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next

        return True
