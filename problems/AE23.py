# Generate Documents

# O(n+m)
# n = len(characters) | m = len(document)

def generateDocument(characters, document):
    counter = {}
	for char in characters:
		if char in counter:
			counter[char] += 1
		else:
			counter[char] = 1
			
	for char in document:
		if not char in counter or counter[char] <= 0:
			return False
		counter[char] -= 1
	return True
