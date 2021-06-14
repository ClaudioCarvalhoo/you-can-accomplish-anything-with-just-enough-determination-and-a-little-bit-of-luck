# O(n²)
# n = n


class Solution:
    def unhappyFriends(
        self, n: int, preferences: List[List[int]], pairs: List[List[int]]
    ) -> int:
        preferenceLevel = {}
        for i in range(len(preferences)):
            preferenceLevel[i] = {}
            for j in range(len(preferences[i])):
                preferenceLevel[i][preferences[i][j]] = j

        satisfactionWithPair = {}
        for pair in pairs:
            satisfactionWithPair[pair[0]] = preferenceLevel[pair[0]][pair[1]]
            satisfactionWithPair[pair[1]] = preferenceLevel[pair[1]][pair[0]]

        res = 0
        for i in preferenceLevel:
            for j in range(satisfactionWithPair[i]):
                betterPair = preferences[i][j]
                if preferenceLevel[betterPair][i] < satisfactionWithPair[betterPair]:
                    res += 1
                    break
        return res