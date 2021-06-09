# O(n)
# n = len(head)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Sol 1
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        preHead = ListNode(None, head)
        node = preHead
        while node.next is not None:
            deleteNext = False
            while node.next.next is not None and node.next.next.val == node.next.val:
                deleteNext = True
                node.next.next = node.next.next.next
            if deleteNext:
                node.next = node.next.next
            else:
                node = node.next
        return preHead.next


# Sol 2
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        preHead = ListNode(None, head)
        parent = preHead
        node = head
        while node is not None:
            deleteNode = False
            while node.next is not None and node.next.val == node.val:
                deleteNode = True
                node.next = node.next.next
            if deleteNode:
                parent.next = node.next
                node = parent.next
            else:
                parent = node
                node = node.next
        return preHead.next
