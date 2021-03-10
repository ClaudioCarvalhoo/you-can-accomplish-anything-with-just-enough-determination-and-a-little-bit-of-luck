# Class Photos

# O(n*log(n))
# n = len(redShirtHeights)

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
	blueShirtHeights.sort()
	
	backRow = redShirtHeights if redShirtHeights[0] > blueShirtHeights[0] else blueShirtHeights
	frontRow = redShirtHeights if redShirtHeights[0] <= blueShirtHeights[0] else blueShirtHeights
	
	for i in range(len(backRow)):
		if backRow[i] <= frontRow[i]:
			return False
	return True
