# Monotonic Array

# O(n)
# n = len(array)

def isMonotonic(array):
    if len(array) <= 1:
		return True
	
	direction = array[-1] - array[0]
	for i in range(1, len(array)):
		difference = array[i] - array[i-1] 
		if (
			(direction > 0 and difference < 0) or 
			(direction < 0 and difference > 0) or 
			(direction == 0 and difference != 0)
		):
			return False
	return True
