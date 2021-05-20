# O(n)
# n = len(distance)


class Solution:
    def distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        clockwiseDist = 0
        i = start
        while i % len(distance) != destination:
            clockwiseDist += distance[i % len(distance)]
            i += 1

        counterClockwiseDist = 0
        i = start
        while i % len(distance) != destination:
            counterClockwiseDist += distance[(i - 1) % len(distance)]
            i -= 1

        return min(clockwiseDist, counterClockwiseDist)