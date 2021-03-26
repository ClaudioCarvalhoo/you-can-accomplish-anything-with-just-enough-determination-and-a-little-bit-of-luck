# Task Assignment

# O(n*log(n))
# n = len(tasks)

def taskAssignment(k, tasks):
    tasks = [(i, tasks[i]) for i in range(len(tasks))]
	tasks.sort(key=lambda x: x[1])
	
	res = []
	for i in range(len(tasks)//2):
		res.append([tasks[i][0], tasks[len(tasks)-i-1][0]])
	return res
