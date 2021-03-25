# Levenshtein Distance

# O(n*m)
# n = len(str1) | m = len(str2)

# Sol 1
# Space Complexity of O(n*m)
def levenshteinDistance(str1, str2):
    if len(str1) <= 0 or len(str2) <= 0:
        return max(len(str1), len(str2))

    numberOfColumns = len(str1) + 1
    numberOfRows = len(str2) + 1
    res = [[float("inf") for _ in range(numberOfColumns)] for _ in range(numberOfRows)]
    res[0] = list(range(numberOfColumns))
    for i in range(numberOfRows):
        res[i][0] = i

    for i in range(1, numberOfRows):
        for j in range(1, numberOfColumns):
            if str1[j - 1] == str2[i - 1]:
                res[i][j] = res[i - 1][j - 1]
            else:
                res[i][j] = 1 + min(res[i - 1][j - 1], res[i - 1][j], res[i][j - 1])

    return res[-1][-1]


# Sol 2
# Space Complexity of O(min(n, m))
def levenshteinDistance(str1, str2):
    if len(str1) <= 0 or len(str2) <= 0:
        return max(len(str1), len(str2))

    str1, str2 = min(str1, str2), max(str1, str2)

    prevSol = list(range(len(str1) + 1))
    for i in range(1, len(str2) + 1):
        curSol = [i]
        for j in range(1, len(str1) + 1):
            if str1[j - 1] == str2[i - 1]:
                curSol.append(prevSol[j - 1])
            else:
                curSol.append(1 + min(prevSol[j - 1], prevSol[j], curSol[j - 1]))
        prevSol = curSol

    return curSol[-1]
