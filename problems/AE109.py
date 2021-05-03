# Ambiguous Measurements

# O(n*low*high)
# n = len(cups)


def ambiguousMeasurements(cups, low, high):
    return explore(cups, 0, 0, low, high, set())


def explore(cups, curLow, curHigh, targetLow, targetHigh, visited):
    if (curLow, curHigh) in visited:
        return False
    visited.add((curLow, curHigh))
    if curLow >= targetLow and curHigh <= targetHigh:
        return True
    if curHigh > targetHigh:
        return False
    for cup in cups:
        if explore(
            cups, curLow + cup[0], curHigh + cup[1], targetLow, targetHigh, visited
        ):
            return True
    return False
