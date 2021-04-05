# Merge Linked Lists

# O(n+m)
# n = len(linkedList1) | m = len(linkedList2)

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
	resHead = LinkedList(None)
	cur = resHead
    while headOne is not None or headTwo is not None:
		if headOne is None:
			cur.next = headTwo
			headTwo = headTwo.next
		elif headTwo is None:
			cur.next = headOne
			headOne = headOne.next
		else:
			if headOne.value <= headTwo.value:
				cur.next = headOne
				headOne = headOne.next
			else:
				cur.next = headTwo
				headTwo = headTwo.next
		cur = cur.next
	return resHead.next