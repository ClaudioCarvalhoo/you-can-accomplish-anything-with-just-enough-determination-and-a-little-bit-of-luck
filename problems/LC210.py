# O(n+p)
# n = numCourses | p = len(prerequisites)


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prerequisitesDict = self.buildPrerequisitesDict(prerequisites, numCourses)
        visited = set()
        order = []
        for course in prerequisitesDict:
            if not self.explore(course, prerequisitesDict, visited, set(), order):
                return []
        return order

    def explore(self, course, prerequisitesDict, visited, loop, order):
        if course in visited:
            return True
        if course in loop:
            return False
        loop.add(course)
        for prerequisite in prerequisitesDict[course]:
            if not self.explore(prerequisite, prerequisitesDict, visited, loop, order):
                loop.remove(course)
                return False
        loop.remove(course)
        order.append(course)
        visited.add(course)
        return True

    def buildPrerequisitesDict(self, prerequisites, numCourses):
        prerequisitesDict = {i: [] for i in range(numCourses)}
        for prerequisite in prerequisites:
            prerequisitesDict[prerequisite[0]].append(prerequisite[1])
        return prerequisitesDict
