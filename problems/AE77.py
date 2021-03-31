# Min Rewards

# O(n)
# n = len(scores)

def minRewards(scores):
    rewards = [1 for _ in scores]
	for i in range(1, len(scores)):
		if scores[i] > scores[i-1]:
			rewards[i] = rewards[i-1] + 1
	for i in range(len(scores)-2, -1, -1):
		if scores[i] > scores[i+1]:
			rewards[i] = max(rewards[i], rewards[i+1]+1)
	return sum(rewards)
