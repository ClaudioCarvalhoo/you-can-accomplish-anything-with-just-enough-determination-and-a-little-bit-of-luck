# O(n*min(n,m))
# n = len(equations) | m = len(queries)


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        connections = {}
        self.buildDefaultConnections(equations, values, connections)
        res = []
        for query in queries:
            if query[0] in connections and query[1] in connections:
                res.append(
                    self.buildConnectionBetween(query[0], query[1], connections, set())
                )
            else:
                res.append(-1.0)
        return res

    def buildDefaultConnections(self, equations, values, connections):
        for i in range(len(equations)):
            val1, val2 = equations[i]
            if val1 not in connections:
                connections[val1] = {val1: 1}
            if val2 not in connections:
                connections[val2] = {val2: 1}
            connections[val1][val2] = values[i]
            connections[val2][val1] = 1 / values[i]

    def buildConnectionBetween(self, val1, val2, connections, visited):
        if val2 in connections[val1]:
            return connections[val1][val2]

        visited.add(val1)
        for nextVal in connections[val1]:
            if nextVal not in visited:
                nextValConnection = self.buildConnectionBetween(
                    nextVal, val2, connections, visited
                )
                if nextValConnection != -1.0:
                    connections[val1][val2] = (
                        connections[val1][nextVal] * nextValConnection
                    )
                    connections[val2][val1] = 1 / (
                        connections[val1][nextVal] * nextValConnection
                    )
                    return connections[val1][val2]
        return -1.0