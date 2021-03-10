# Minimum Waiting Time

# O(n)
# n = len(queries)

def minimumWaitingTime(queries):
    queries.sort()
	total = 0
	res = 0
	for query in queries:
		res += total
		total += query
	return res
