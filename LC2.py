# O(n+m)
# n = len(l1) | m = len(l2)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        resHead = ListNode(None)
        resCur = resHead
        carry = 0
        while l1 is not None or l2 is not None or carry > 0:
            current = carry
            if l1 is not None:
                current += l1.val
                l1 = l1.next
            if l2 is not None:
                current += l2.val
                l2 = l2.next
            carry = current // 10
            current = current % 10
            resCur.next = ListNode(current)
            resCur = resCur.next
        return resHead.next