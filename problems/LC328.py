# O(n) Time | O(1) Space
# n = len(head)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        evenHead = head.next
        curOdd = head
        curEven = evenHead
        while curEven is not None and curEven.next is not None:
            curOdd.next = curEven.next
            curOdd = curOdd.next
            curEven.next = curOdd.next
            curEven = curEven.next
        curOdd.next = evenHead
        return head
