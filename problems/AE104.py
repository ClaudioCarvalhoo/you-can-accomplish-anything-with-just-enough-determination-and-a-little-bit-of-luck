# Lowest Common Manager

# O(n)
# n = numberOfNodesBelow(topManager)


def getLowestCommonManager(topManager, reportOne, reportTwo):
    pathToOne = findAndGetPath(topManager, reportOne, [topManager])[1]
    pathToTwo = findAndGetPath(topManager, reportTwo, [topManager])[1]
    startSearch = min(len(pathToOne), len(pathToTwo)) - 1
    for i in range(startSearch, -1, -1):
        if pathToOne[i] == pathToTwo[i]:
            return pathToOne[i]


def findAndGetPath(current, target, pathSoFar):
    if current == target:
        return (True, pathSoFar)
    for report in current.directReports:
        pathSoFar.append(report)
        possiblePath = findAndGetPath(report, target, pathSoFar)
        if possiblePath[0]:
            return possiblePath
        pathSoFar.pop()
    return (False, None)


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
