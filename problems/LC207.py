# O(n+m)
# n = numCourses | m = len(prerequisitesList)


class Solution:
    def canFinish(self, numCourses: int, prerequisitesList: List[List[int]]) -> bool:
        prerequisites = {}
        for prerequisite in prerequisitesList:
            if prerequisite[0] not in prerequisites:
                prerequisites[prerequisite[0]] = set()
            prerequisites[prerequisite[0]].add(prerequisite[1])

        visited = set()
        for i in range(numCourses):
            if not self.explore(i, visited, set(), prerequisites):
                return False
        return True

    def explore(self, i, visited, inLoop, prerequisites):
        if i in visited:
            return True
        if i in inLoop:
            return False

        inLoop.add(i)
        if i in prerequisites:
            for j in prerequisites[i]:
                if not self.explore(j, visited, inLoop, prerequisites):
                    return False
        inLoop.remove(i)
        visited.add(i)
        return True