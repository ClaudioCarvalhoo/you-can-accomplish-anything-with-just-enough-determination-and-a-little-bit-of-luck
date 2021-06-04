# O(n*log(n)) Time | O(1) Space
# n = len(head)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        listLen = 0
        cur = head
        while cur is not None:
            cur = cur.next
            listLen += 1

        if listLen == 0 or listLen == 1:
            return head

        head = ListNode(None, head)
        chunkLen = 1
        while chunkLen < listLen:
            prev = head
            remaining = listLen
            while prev.next is not None:
                l1ChunkLen = min(chunkLen, remaining)
                l2ChunkLen = min(chunkLen, remaining - l1ChunkLen)
                l1 = prev.next
                l2 = prev.next
                for _ in range(l1ChunkLen):
                    l2 = l2.next
                chunkEnd = self.mergeInPlace(prev, l1, l1ChunkLen, l2, l2ChunkLen)
                prev = chunkEnd
                remaining -= l1ChunkLen + l2ChunkLen
            chunkLen *= 2
        return head.next

    def mergeInPlace(self, prev, l1, l1ChunkLen, l2, l2ChunkLen):
        if l1 == l2:
            return l1
        chunkEnd = l2
        for _ in range(l2ChunkLen):
            chunkEnd = chunkEnd.next
        l1Cur, l2Cur = 0, 0
        while l1Cur < l1ChunkLen or l2Cur < l2ChunkLen:
            if l1Cur >= l1ChunkLen:
                prev.next = l2
                l2 = l2.next
                l2Cur += 1
            elif l2Cur >= l2ChunkLen:
                prev.next = l1
                l1 = l1.next
                l1Cur += 1
            elif l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
                l1Cur += 1
            else:
                prev.next = l2
                l2 = l2.next
                l2Cur += 1
            prev = prev.next
        prev.next = chunkEnd
        return prev
