# Knapsack Problem

# O(n*c)
# n = len(items) | c = capacity

def knapsackProblem(items, capacity):
    res = [[0 for _ in range(capacity+1)] for _ in range(len(items)+1)]
	for i in range(1, len(res)):
		weigth = items[i-1][1]
		value = items[i-1][0]
		for c in range(1, len(res[i])):
			if weigth > c:
				res[i][c] = res[i-1][c]
			else:
				res[i][c] = max(res[i-1][c], value + res[i-1][c-weigth])
				
	i = len(res)-1
	c = len(res[i])-1
	knapsack = []
	while i > 0 and c > 0:
		if res[i-1][c] != res[i][c]:
			knapsack.append(i-1)
			c -= items[i-1][1]
		i -= 1
	return [res[-1][-1], knapsack]
			