# Topological Sort

# O(j+d)
# j = len(jobs) | d = len(deps)

def topologicalSort(jobs, deps):
    completed = set()
	dependsOn = {j: set() for j in jobs}
	for d in deps:
		dependsOn[d[1]].add(d[0])
		
	res = []
	for j in jobs:
		explore(completed, set(), dependsOn, j, res)
	
	if len(res) == len(jobs):
		return res
	else:
		return []

def explore(completed, loopDetection, dependsOn, cur, res):
	if cur in loopDetection:
		return False
	if cur in completed:
		return True
	loopDetection.add(cur)
	for dependency in dependsOn[cur]:
		canUnlock = explore(completed, loopDetection, dependsOn, dependency, res)
		if not canUnlock:
			return False
	loopDetection.remove(cur)
	completed.add(cur)
	res.append(cur)
	return True
	