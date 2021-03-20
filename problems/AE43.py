# Number Of Ways To Make Change

# O(n*c)
# n = n | c = len(coins)

def numberOfWaysToMakeChange(n, coins):
    possibilities = [0 for _ in range(n+1)]
	possibilities[0] = 1
	
	for coin in coins:
		for i in range(coin, n+1):
			necessary = i - coin
			possibilities[i] += possibilities[necessary]

	return possibilities[-1]
