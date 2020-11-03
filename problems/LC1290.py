# O(n)
# n = len(head)

# Space: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        while head != None:
            num <<= 1
            num |= head.val
            head = head.next
        return num
            
                