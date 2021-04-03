# Boggle Board

# O(w*s+n*m*8ˢ)
# w = len(words) | s = stringWithMaxLength(words)
# n = len(board) | m = len(board[0])

def boggleBoard(board, words):
    trie = {}
	for word in words:
		trieNode = trie
		for letter in word:
			if letter not in trieNode:
				trieNode[letter] = {}
			trieNode = trieNode[letter]
		trieNode["END"] = True
		
	res = set()
	for y in range(len(board)):
		for x in range(len(board[y])):
			explore(board, y, x, trie, res, [], set())
	return list(res)

def explore(board, y, x, trie, res, cur, used):
	if y < 0 or y >= len(board) or x < 0 or x >= len(board[y]) or (y, x) in used:
		return
	letter = board[y][x]
	if letter not in trie:
		return
	cur.append(letter)
	used.add((y, x))
	trie = trie[letter]
	if "END" in trie:
		res.add(''.join(cur))
	for nextY in range(-1, 2):
		for nextX in range(-1, 2):
			if nextX == 0 and nextY == 0:
				continue
			explore(board, y + nextY, x + nextX, trie, res, cur, used)
	cur.pop()
	used.remove((y, x))