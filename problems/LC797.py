# O(2ⁿ*n)
# n = len(graph)


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.explore(graph, 0, [], res)
        return res

    def explore(self, graph, curNode, path, res):
        path.append(curNode)
        if curNode == len(graph) - 1:
            res.append(path[:])
        else:
            for adjNode in graph[curNode]:
                self.explore(graph, adjNode, path, res)
        path.pop()