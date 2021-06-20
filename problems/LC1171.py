# O(n)
# n = len(head)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        preHead = ListNode(float("inf"), head)
        runningSumToNode = {0: preHead}

        node = head
        runningSum = 0
        while node is not None:
            runningSum += node.val
            if runningSum in runningSumToNode:
                self.removeBetween(runningSum, node, runningSumToNode)
            else:
                runningSumToNode[runningSum] = node
            node = node.next
        return preHead.next

    def removeBetween(self, runningSum, destination, runningSumToNode):
        parent = runningSumToNode[runningSum]
        node = parent.next
        while node != destination:
            runningSum += node.val
            del runningSumToNode[runningSum]
            node = node.next
        parent.next = node.next