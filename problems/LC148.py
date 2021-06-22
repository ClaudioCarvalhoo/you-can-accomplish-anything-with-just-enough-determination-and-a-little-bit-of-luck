# O(n*log(n)) Time | O(1) Space
# n = len(head)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        listLen = self.findListLen(head)
        if listLen <= 1:
            return head

        preHead = ListNode(float("-inf"), head)
        self.mergeSort(preHead, listLen)
        return preHead.next

    def findListLen(self, head):
        listLen = 0
        node = head
        while node is not None:
            listLen += 1
            node = node.next
        return listLen

    def mergeSort(self, prev, listLen):
        if listLen == 1:
            return prev.next
        leftSize = math.floor(listLen / 2)
        rightSize = math.ceil(listLen / 2)
        midPrev = self.mergeSort(prev, leftSize)
        end = self.mergeSort(midPrev, rightSize).next
        return self.mergeInPlace(prev, leftSize, midPrev, rightSize, end)

    def mergeInPlace(self, leftPrev, leftSize, rightPrev, rightSize, end):
        prev = leftPrev
        left = leftPrev.next
        right = rightPrev.next
        while leftSize > 0 and rightSize > 0:
            if left.val <= right.val:
                prev.next = left
                leftSize -= 1
                left = left.next
            else:
                prev.next = right
                rightSize -= 1
                right = right.next
            prev = prev.next
        while leftSize > 0:
            prev.next = left
            leftSize -= 1
            prev = prev.next
            left = left.next
        while rightSize > 0:
            prev.next = right
            rightSize -= 1
            prev = prev.next
            right = right.next
        prev.next = end
        return prev