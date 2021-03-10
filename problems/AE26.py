# Move Element To End

# O(n)
# n = len(array)


def moveElementToEnd(array, toMove):
    end = calculateNewEnd(array, toMove, len(array) - 1)
    if end < 0:
        return array

    for i in range(len(array)):
        if array[i] == toMove:
            swap(array, i, end)
            end = calculateNewEnd(array, toMove, end - 1)
        if end <= i:
            break
    return array


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def calculateNewEnd(array, toMove, end):
    while end >= 0 and array[end] == toMove:
        end -= 1
    return end
