# Merge Overlapping Intervals

# O(n*log(n))
# n = len(intervals)

def mergeOverlappingIntervals(intervals):
    res = []
	intervals.sort(key=lambda interval: interval[0])
	
	i = 0
	while i < len(intervals):
		res.append(intervals[i])
		j = i+1
		while j < len(intervals) and res[-1][1] >= intervals[j][0]:
			res[-1][1] = max(res[-1][1], intervals[j][1])
			j += 1
		i = j
		
	return res
