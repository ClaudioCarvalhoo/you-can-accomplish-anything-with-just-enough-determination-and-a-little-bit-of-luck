# Tandem Bicycle

# O(n*log(n))
# n = len(redShirtSpeeds)

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
	blueShirtSpeeds.sort()
	fastestPossible = 0
	slowestPossible = 0
	for i in range(len(redShirtSpeeds)):
		slowestPossible += max(redShirtSpeeds[i], blueShirtSpeeds[i])
		fastestPossible += max(redShirtSpeeds[i], blueShirtSpeeds[-i-1])
	return fastestPossible if fastest else slowestPossible