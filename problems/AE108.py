# Generate Div Tags

def generateDivTags(numberOfTags):
    res = []
	helper([], 0, numberOfTags, res)
	return res
	
def helper(cur, openTags, remainingTags, res):
	if remainingTags == 0 and openTags == 0:
		res.append(build(cur))
		return
	
	if remainingTags > 0:
		cur.append(True)
		helper(cur, openTags+1, remainingTags-1, res)
		cur.pop()
	if openTags > 0:
		cur.append(False)
		helper(cur, openTags-1, remainingTags, res)
		cur.pop()
		
	
def build(elems):
	res = []
	for elem in elems:
		if elem:
			res += ['<','d','i','v','>']
		else:
			res += ['<','/','d','i','v','>']
	return ''.join(res)
	
