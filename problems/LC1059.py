# O(v+e)
# v = n | e = len(edges)


class Solution:
    def leadsToDestination(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        goesTo = self.buildGoesTo(n, edges)
        return self.explore(source, goesTo, destination, {}, set())

    def explore(self, node, goesTo, destination, dp, visited):
        if node in dp:
            return dp[node]
        if len(goesTo[node]) == 0:
            return node == destination
        visited.add(node)
        for adjNode in goesTo[node]:
            if adjNode in visited or not self.explore(
                adjNode, goesTo, destination, dp, visited
            ):
                dp[node] = False
                return False
        visited.remove(node)
        dp[node] = True
        return True

    def buildGoesTo(self, n, edges):
        goesTo = {}
        for node in range(n):
            goesTo[node] = []
        for edge in edges:
            goesTo[edge[0]].append(edge[1])
        return goesTo