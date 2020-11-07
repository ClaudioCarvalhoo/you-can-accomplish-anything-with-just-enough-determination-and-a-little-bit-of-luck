# O(n + m)
# n = len(l1) | m = len(l2)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number1 = self.linkedAsInt(l1)
        number2 = self.linkedAsInt(l2)
        res = number1 + number2
        node = ListNode()
        while res > 0:
            digit = res % 10
            node.val = digit
            res = res // 10
            if res <= 0:
                break
            node = ListNode(next=node)
        return node

    def linkedAsInt(self, listNode):
        number = 0
        while listNode != None:
            number *= 10
            number += listNode.val
            listNode = listNode.next
        return number