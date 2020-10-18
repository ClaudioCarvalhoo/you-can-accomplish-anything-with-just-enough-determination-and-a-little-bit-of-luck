# O(n)
# n = len(answers)


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        found = {}
        for i in answers:
            if i in found:
                found[i] += 1
            else:
                found[i] = 1

        total = 0
        for j in found:
            n = j + 1
            if found[j] <= n:
                total += n
            else:
                total += n * int(found[j] / n)
                if found[j] % n != 0:
                    total += n

        return total