# O(v+e)
# v = vertices(graph) | e = edges(graph)

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        nodeMapper = {None: None}
        return self.cloneNode(node, nodeMapper)

    def cloneNode(self, node, nodeMapper):
        if node in nodeMapper:
            return nodeMapper[node]
        nodeMapper[node] = Node(node.val)
        for neighbor in node.neighbors:
            nodeMapper[node].neighbors.append(self.cloneNode(neighbor, nodeMapper))
        return nodeMapper[node]