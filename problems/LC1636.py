# O(n * log(n))
# n = len(nums)


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        numsWithFrequency = []
        for i in nums:
            numsWithFrequency.append((i, counter[i]))

        numsWithFrequency.sort(key=lambda x: (x[1], -1 * x[0]))

        res = [x[0] for x in numsWithFrequency]

        return res