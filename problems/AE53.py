# Cycle In Graph

# O(v + e)
# v = vertices | e = edges

def cycleInGraph(edges):
    visited = set()
	for i in range(len(edges)):
		if i not in visited:
			if explore(edges, i, set(), visited):
				return True
	return False

def explore(edges, i, possibleCycle, visited):
	if i in possibleCycle:
		return True
	else:
		visited.add(i)
		possibleCycle.add(i)
		for adjacent in edges[i]:
			if explore(edges, adjacent, possibleCycle, visited):
				return True
		possibleCycle.remove(i)
		return False