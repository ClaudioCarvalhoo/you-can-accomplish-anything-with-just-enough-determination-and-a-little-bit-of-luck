# Min Number Of Coins For Change

# O(n*c)
# n = n | c = len(coins)


def minNumberOfCoinsForChange(n, coins):
    minAmounts = [float("inf") for _ in range(n + 1)]
    minAmounts[0] = 0

    for i in range(1, n + 1):
        for coin in coins:
            if coin <= i:
                minAmounts[i] = min(minAmounts[i], minAmounts[i - coin] + 1)

    if minAmounts[-1] == float("inf"):
        return -1
    else:
        return minAmounts[-1]
