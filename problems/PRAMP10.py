# BST Successor Search
# In a Binary Search Tree (BST), an Inorder Successor of a node is defined as
# the node with the smallest key greater than the key of the input node (see examples below).
# Given a node inputNode in a BST, you’re asked to write a function findInOrderSuccessor
# that returns the Inorder Successor of inputNode.
# If inputNode has no Inorder Successor, return null.

# Explain your solution and analyze its time and space complexities.

# Time
# O(h)
# h = height(tree)

# Space
# O(1)

# Most of the code below is default from the question.
# I only implemented the find_in_order_successor method and the find_leftmost_child helper method.


#########################################################
# CODE INSTRUCTIONS:                                    #
# 1) The method findInOrderSuccessor you're asked      #
#    to implement is located at line 30.                #
# 2) Use the helper code below to implement it.         #
# 3) In a nutshell, the helper code allows you to       #
#    to build a Binary Search Tree.                     #
# 4) Jump to line 88 to see an example for how the      #
#    helper code is used to test findInOrderSuccessor.  #
#########################################################


# A node
class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


# A binary search tree
class BinarySearchTree:

    # Constructor to create a new BST
    def __init__(self):
        self.root = None

    """
  case 1:
    I have a right child
      go to right child -> go all the way to the left
  case 2:
    I don't have a right child
    loop:
      Go to the parent
      if i came from the left -> return parent
      if parent is null -> return null
    
  """

    def find_in_order_successor(self, inputNode):
        if inputNode is None:
            return None
        if inputNode.right is not None:
            return self.find_leftmost_child(inputNode.right)
        else:
            while inputNode.parent is not None:
                if inputNode.parent.left == inputNode:
                    return inputNode.parent
                else:
                    inputNode = inputNode.parent
            return None

    def find_leftmost_child(self, node):
        while node.left is not None:
            node = node.left
        return node

    # Given a binary search tree and a number, inserts a
    # new node with the given number in the correct place
    # in the tree. Returns the new root pointer which the
    # caller should then use(the standard trick to avoid
    # using reference parameters)
    def insert(self, key):

        # 1) If tree is empty, create the root
        if self.root is None:
            self.root = Node(key)
            return

        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        currentNode = self.root
        newNode = Node(key)
        while currentNode is not None:

            if key < currentNode.key:
                if currentNode.left is None:
                    currentNode.left = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.right

    # Return a reference to a node in the BST by its key.
    # Use this method when you need a node to test your
    # findInOrderSuccessor function on
    def getNodeByKey(self, key):

        currentNode = self.root
        while currentNode is not None:
            if key == currentNode.key:
                return currentNode

            if key < currentNode.key:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        return None


#########################################
# Driver program to test above function #
#########################################

# Create a Binary Search Tree
bst = BinarySearchTree()
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(14)

# Get a reference to the node whose key is 9
test = bst.getNodeByKey(9)

# Find the in order successor of test
succ = bst.find_in_order_successor(test)

# Print the key of the successor node
if succ is not None:
    print("\nInorder Successor of %d is %d " % (test.key, succ.key))
else:
    print("\nInorder Successor doesn't exist")
