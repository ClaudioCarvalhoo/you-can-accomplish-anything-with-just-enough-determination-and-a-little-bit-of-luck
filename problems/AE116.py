# O(n*log(n))
# n = len(array)


def heapSort(array):
    for i in range(len(array) - 1, -1, -1):
        siftDown(array, i, len(array) - 1)

    for i in range(len(array) - 1, -1, -1):
        siftDown(array, 0, i)
        swap(array, 0, i)

    return array


def siftDown(array, heapStart, heapEnd):
    i = heapStart
    childrenIndexes = getChildrenIndexes(array, i)
    while len(childrenIndexes) > 0:
        bestChildIndex = None
        bestChild = float("-inf")
        for childIndex in childrenIndexes:
            if (
                childIndex <= heapEnd
                and array[childIndex] > array[i]
                and array[childIndex] > bestChild
            ):
                bestChild = array[childIndex]
                bestChildIndex = childIndex
        if bestChildIndex is None:
            break
        else:
            swap(array, i, bestChildIndex)
            i = bestChildIndex
            childrenIndexes = getChildrenIndexes(array, i)


def getParentIndex(array, i):
    return max(0, ((i - 2) // 2))


def getChildrenIndexes(array, i):
    return [(i * 2) + 1, (i * 2) + 2]


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
