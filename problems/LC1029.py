# O(n*log(n))
# n = len(costs)

# Sol 1
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = [(abs(cost[0] - cost[1]), cost) for cost in costs]
        costs.sort(key=lambda x: x[0], reverse=True)

        res = 0
        goingToA = 0
        goingToB = 0
        for _, cost in costs:
            if goingToB >= len(costs) // 2 or (
                cost[0] <= cost[1] and goingToA < len(costs) // 2
            ):
                res += cost[0]
                goingToA += 1
            else:
                res += cost[1]
                goingToB += 1
        return res


# Sol 2
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])

        res = 0
        for i in range(len(costs)):
            res += costs[i][0] if i < len(costs) // 2 else costs[i][1]
        return res