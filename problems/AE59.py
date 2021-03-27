# Sum of Linked Lists

# O(max(n, m))
# n = len(linkedListOne) | m = len(linkedListTwo)

def sumOfLinkedLists(linkedListOne, linkedListTwo):
    res = LinkedList(None)
	curRes = res
	curOne = linkedListOne
	curTwo = linkedListTwo
	carry = 0
	while curOne or curTwo or carry > 0:
		val1 = 0
		val2 = 0
		if curOne:
			val1 = curOne.value
			curOne = curOne.next
		if curTwo:
			val2 = curTwo.value
			curTwo = curTwo.next
		sumVal = val1 + val2 + carry
		carry = sumVal // 10
		curRes.next = LinkedList(sumVal % 10)
		curRes = curRes.next
	return res.next