# Max Sum Increasing Subsequence

# O(n²)
# n = len(array)


def maxSumIncreasingSubsequence(array):
    bestSum = float("-inf")
    bestSubsequenceFrom = -1
    startingFrom = [0 for _ in array]
    afterThis = [None for _ in array]
    for i in range(len(array) - 1, -1, -1):
        currentBest = array[i]
        currentBestNext = None
        for skipTo in range(i + 1, len(array)):
            if array[skipTo] > array[i]:
                if array[i] + startingFrom[skipTo] > currentBest:
                    currentBest = array[i] + startingFrom[skipTo]
                    currentBestNext = skipTo
        startingFrom[i] = currentBest
        afterThis[i] = currentBestNext
        if currentBest > bestSum:
            bestSum = currentBest
            bestSubsequenceFrom = i

    subsequence = [bestSubsequenceFrom]
    while afterThis[subsequence[-1]]:
        subsequence.append(afterThis[subsequence[-1]])
    subsequence = [array[x] for x in subsequence]

    return [bestSum, subsequence]
