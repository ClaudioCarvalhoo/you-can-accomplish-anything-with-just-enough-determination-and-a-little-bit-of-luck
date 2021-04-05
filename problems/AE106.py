# Solve Sudoku

# O(1)

def solveSudoku(board):
	completeDigits = set([1,2,3,4,5,6,7,8,9])
    rows = [set() for _ in range(9)]
	columns = [set() for _ in range(9)]
	subgrids = [set() for _ in range(9)]
	
	for y in range(9):
		for x in range(9):
			current = board[y][x]
			if current != 0:
				rows[y].add(current)
				columns[x].add(current)
				subgrids[subgridIndex(y, x)].add(current)
	
	fill(board, 0, 0, rows, columns, subgrids, completeDigits)
		
	return board

def fill(board, y, x, rows, columns, subgrids, completeDigits):
	if y >= 9:
		return True
	
	nextCell = (y + ((x+1)//9), (x+1)%9)
	if board[y][x] == 0:
		possibilities = completeDigits.difference(rows[y], columns[x], subgrids[subgridIndex(y, x)])
		for num in possibilities:
			rows[y].add(num)
			columns[x].add(num)
			subgrids[subgridIndex(y, x)].add(num)
			board[y][x] = num
			works = fill(board, nextCell[0], nextCell[1], rows, columns, subgrids, completeDigits)
			if works:
				return True
			else:
				rows[y].remove(num)
				columns[x].remove(num)
				subgrids[subgridIndex(y, x)].remove(num)
				board[y][x] = 0
		return False	
	else:
		return fill(board, nextCell[0], nextCell[1], rows, columns, subgrids, completeDigits)
	
	
def subgridIndex(y, x):
	if y < 3:
		return x//3
	elif y < 6:
		return 3 + x//3
	else:
		return 6 + x//3
	