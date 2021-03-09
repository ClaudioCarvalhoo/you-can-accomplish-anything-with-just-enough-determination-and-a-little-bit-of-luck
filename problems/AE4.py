# Tournament Winner

# O(n)
# n = len(competitions)

def tournamentWinner(competitions, results):
    points = {}
	for i in range(len(competitions)):
		winner = competitions[i][results[i]-1]
		if winner in points:
			points[winner] += 3
		else:
			points[winner] = 3
			
	champion = (None, 0)
	for team in points:
		if points[team] >= champion[1]:
			champion = (team, points[team])
	return champion[0]
