# Laptop Rentals

# O(n*log(n))
# n = len(times)

import heapq

def laptopRentals(times):
    times.sort(key = lambda x: x[0])
	
	heap = []
	for i in range(len(times)):
		if len(heap) > 0 and times[i][0] >= heap[0]:
			heapq.heappop(heap)
			heapq.heappush(heap, times[i][1])
		else:
			heapq.heappush(heap, times[i][1])
			
	return len(heap)