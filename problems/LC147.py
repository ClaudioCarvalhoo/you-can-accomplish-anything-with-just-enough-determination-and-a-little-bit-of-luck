# O(n²)
# n = len(head)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        head = ListNode(float("-inf"), head)
        prev = head
        cur = head.next
        while cur != None: 
            prev.next = cur.next
            nxt = prev.next
            scout = head
            while scout.next != None and scout.next.val < cur.val and scout != prev:
                scout = scout.next
            if scout.next == None:
                temp = None
            else:
                temp = scout.next
            scout.next = cur
            cur.next = temp
            cur = nxt
            while scout.next != cur:
                scout = scout.next
            prev = scout
        return head.next