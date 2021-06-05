# O(n)
# n = len(gas)


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasGain = [gas[i] - cost[i] for i in range(len(gas))]

        tank = 0
        routeLen = 0
        for i in range(len(gasGain) * 2):
            if routeLen == len(gas):
                return i - len(gas)
            tank += gasGain[i % len(gasGain)]
            if tank < 0:
                tank = 0
                routeLen = 0
            else:
                routeLen += 1
        return -1
