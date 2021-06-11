# O(n*k) considering only 26 characters
# n = len(words) | k = maxLen(words)


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        orderedTrie = self.buildOrderedTrie(words)
        if orderedTrie is None:
            return ""
        relationalOrders = self.getRelationalOrders(orderedTrie)
        graph = self.buildGraph(relationalOrders)
        return "".join(self.topologicalSort(graph))

    def buildOrderedTrie(self, words):
        root = {"order": []}
        for word in words:
            node = root
            for i in range(len(word)):
                char = word[i]
                if char not in node:
                    node["order"].append(char)
                    node[char] = {"order": []}
                elif i == len(word) - 1 and len(node[char].keys()) > 1:
                    return None
                elif len(node["order"]) > 0 and node["order"][-1] != char:
                    return None
                node = node[char]
        return root

    def getRelationalOrders(self, orderedTrie):
        res = []
        stack = [orderedTrie]
        while len(stack) > 0:
            node = stack.pop()
            if len(node["order"]) > 0:
                res.append(node["order"])
            for key in node:
                if key != "order":
                    stack.append(node[key])
        return res

    def buildGraph(self, relationalOrders):
        graph = {}
        for order in relationalOrders:
            seenBefore = set()
            for char in order:
                if char not in graph:
                    graph[char] = {"precursors": set()}
                graph[char]["precursors"] = graph[char]["precursors"].union(seenBefore)
                seenBefore.add(char)
        return graph

    def topologicalSort(self, graph):
        res = []
        visited = set()
        for char in graph:
            self.topoHelper(graph, char, visited, set(), res)
        return res

    def topoHelper(self, graph, char, visited, loop, res):
        if char in visited:
            return True
        if char in loop:
            return False
        loop.add(char)
        for precursor in graph[char]["precursors"]:
            if not self.topoHelper(graph, precursor, visited, loop, res):
                return False
        loop.remove(char)
        visited.add(char)
        res.append(char)
        return True
