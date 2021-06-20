# O(n)
# n = len(numbers)

# Sol 1 | O(n) Space
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        positions = {}
        for i in range(len(numbers)):
            if numbers[i] not in positions:
                positions[numbers[i]] = []
            positions[numbers[i]].append(i)

        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in positions and positions[complement][-1] != i:
                return [i + 1, positions[complement][-1] + 1]


# Sol 2 | O(1) Space
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            currentSum = numbers[start] + numbers[end]
            if currentSum == target:
                return [start + 1, end + 1]
            elif currentSum > target:
                end -= 1
            else:
                start += 1