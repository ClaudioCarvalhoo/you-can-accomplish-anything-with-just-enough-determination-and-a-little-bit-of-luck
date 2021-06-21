# O(n)
# n = numberOfNodes(root)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        if root is None:
            return []
        res = []
        self._serializeHelper(root, res)
        return "".join(res)

    def _serializeHelper(self, node, res):
        res.append(str(node.val))
        if node.left is not None:
            res.append("l")
            self._serializeHelper(node.left, res)
        if node.right is not None:
            res.append("r")
            self._serializeHelper(node.right, res)
        res.append("b")

    def deserialize(self, data):
        if len(data) == 0:
            return None

        serializedList = []
        curNum = 0
        curNumNegative = False
        for i in range(len(data)):
            char = data[i]
            if char == "[":
                continue
            elif char == "-":
                curNumNegative = True
            elif char.isdigit():
                curNum *= 10
                curNum += int(char)
                if not data[i + 1].isdigit():
                    if curNumNegative:
                        curNum *= -1
                    serializedList.append(curNum)
                    curNum = 0
                    curNumNegative = False
            else:
                serializedList.append(char)

        root = TreeNode(None)
        node = root
        stack = [None]
        for i in range(len(serializedList)):
            if serializedList[i] == "l":
                node.left = TreeNode(None)
                stack.append(node)
                node = node.left
            elif serializedList[i] == "r":
                node.right = TreeNode(None)
                stack.append(node)
                node = node.right
            elif serializedList[i] == "b":
                node = stack.pop()
            else:
                node.val = serializedList[i]
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))