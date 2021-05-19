# Shorten Path

# O(n)
# n = len(path)

def shortenPath(path):	
    stack = []
	i = 0
	if path[0] == '/':
		stack.append('')
		i = 1
	while i < len(path):
		part, i = parsePart(path, i)
		if part == '..':
			if len(stack) <= 0 or stack[-1] == '..':
				stack.append(part)
			elif len(stack[-1]) > 0:
				stack.pop()
		elif len(part) >= 1 and part != '.':
			stack.append(part)
	
	res = '/'.join(stack)
	return res if len(res) > 0 else '/'
		
def parsePart(path, i):
	res = []
	while i < len(path) and path[i] != '/':
		res.append(path[i])
		i += 1
	return (''.join(res), i+1)
