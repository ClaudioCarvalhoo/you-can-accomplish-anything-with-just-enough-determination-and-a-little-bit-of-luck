# Longest Common Subsequence

# O(n*m)
# n = len(str1) | m = len(str2)


def longestCommonSubsequence(str1, str2):
    res = [
        [[None, 0, None, None] for _ in range(len(str1) + 1)]
        for _ in range(len(str2) + 1)
    ]
    for y in range(1, len(str2) + 1):
        for x in range(1, len(str1) + 1):
            if str1[x - 1] == str2[y - 1]:
                res[y][x][0] = str1[x - 1]
                res[y][x][1] = res[y - 1][x - 1][1] + 1
                res[y][x][2], res[y][x][3] = y - 1, x - 1
            else:
                res[y][x] = max(res[y - 1][x], res[y][x - 1], key=lambda x: x[1])

    lcs = []
    cur = res[-1][-1]
    while cur[0] != None:
        lcs.append(cur[0])
        cur = res[cur[2]][cur[3]]
    return list(reversed(lcs))
