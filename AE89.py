# Dijkstra's Algorithm

# O((v+e)*log(v))
# v = numberOfVertices | e = numberOfEdges

import heapq

def dijkstrasAlgorithm(start, edges):
    dists = [float('inf') for _ in edges]
	visited = set()
	
	heap = [(0, start)]
	while len(heap) > 0:
		distance, destination = heapq.heappop(heap)
		if destination not in visited:
			visited.add(destination)
			dists[destination] = distance
			for edge in edges[destination]:
				if edge[0] not in visited:
					heapq.heappush(heap, (edge[1]+distance, edge[0]))
	
	return [dist if dist != float('inf') else -1 for dist in dists]
