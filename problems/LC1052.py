# O(n)
# n = len(customers)


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        dissatisfied = [
            customers[i] if grumpy[i] > 0 else 0 for i in range(len(customers))
        ]

        best = sum(dissatisfied[:X])
        latest = best
        for i in range(X, len(dissatisfied)):
            latest = latest - dissatisfied[i - X] + dissatisfied[i]
            best = max(best, latest)

        return sum(customers) - sum(dissatisfied) + best