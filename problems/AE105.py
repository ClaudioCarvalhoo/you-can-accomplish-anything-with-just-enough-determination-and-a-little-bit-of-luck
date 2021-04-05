# Interweaving Strings

# O(n*m)
# n = len(one) | m = len(two)

def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
		return False
	return explore(one, two, three, 0, 0, {})
    
def explore(one, two, three, p1, p2, cache):
	p3 = p1 + p2
	if p3 >= len(three):
		return True
	
	if (p1, p2) in cache:
		return cache[(p1, p2)]
	
	target = three[p3]
	useOne = False
	useTwo = False
	if canGetLetterFrom(one, p1, target):
		useOne = explore(one, two, three, p1+1, p2, cache)
		cache[(p1+1, p2)] = useOne
	if canGetLetterFrom(two, p2, target):
		useTwo = explore(one, two, three, p1, p2+1, cache)
		cache[(p1, p2+1)] = useTwo
	return useOne or useTwo

def canGetLetterFrom(string, i, letter):
	return i < len(string) and string[i] == letter
