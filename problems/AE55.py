# Valid Starting City

# O(n)
# n = len(distances)

def validStartingCity(distances, fuel, mpg):
	for i in range(len(fuel)):
		fuel[i] = fuel[i]*mpg
	
	currentFuel = 0
	comingFrom = 0
	for i in range(2 * len((distances))):
		if i - comingFrom == len(distances):
			return comingFrom
		
		city = i % len(distances)
		currentFuel += fuel[city]
    	if distances[city] > currentFuel:
			comingFrom = i+1
			currentFuel = 0
		else:
			currentFuel -= distances[city]
	return None