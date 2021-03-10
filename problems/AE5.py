# Non-Constructible Change

# O(n*log(n))
# n = len(coins)

def nonConstructibleChange(coins):
    if len(coins) <= 0:
		return 1
	
	coins.sort()
	upTo = 0
	for coin in coins:
		if upTo < coin-1:
			return upTo+1
		else:
			upTo += coin
	return upTo+1
	