# k + n*log(k)
# k = len(lists) | n = totalNodes(lists)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        preHead = ListNode(None)
        curAnsNode = preHead
        heap = []
        for i in range(len(lists)):
            if lists[i] is not None:
                node = lists[i]
                heap.append((node.val, i, node))
        heapq.heapify(heap)
        while len(heap) > 0:
            _, i, node = heapq.heappop(heap)
            curAnsNode.next = node
            curAnsNode = curAnsNode.next
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return preHead.next