# O(n*log(k))
# n = n | k = len(primes)

import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglyHeap = [(primes[i], i, 0) for i in range(len(primes))]
        superUgly = [1]
        while len(superUgly) < n:
            nextUgly, primeUsed, multiplierIndex = heapq.heappop(uglyHeap)
            superUgly.append(nextUgly)
            multiplierIndex += 1
            heapq.heappush(
                uglyHeap,
                (
                    primes[primeUsed] * superUgly[multiplierIndex],
                    primeUsed,
                    multiplierIndex,
                ),
            )
            while uglyHeap[0][0] <= superUgly[-1]:
                nextUgly, primeUsed, multiplierIndex = heapq.heappop(uglyHeap)
                multiplierIndex += 1
                heapq.heappush(
                    uglyHeap,
                    (
                        primes[primeUsed] * superUgly[multiplierIndex],
                        primeUsed,
                        multiplierIndex,
                    ),
                )
        return superUgly[-1]