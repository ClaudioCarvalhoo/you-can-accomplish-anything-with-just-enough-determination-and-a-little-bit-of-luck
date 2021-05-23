import heapq

# Sol 1 - Heap
# O(n*log(k))
# n = len(nums) | k = k
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        heap = []
        for num in counter.keys():
            heapq.heappush(heap, (counter[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [elem[1] for elem in heap]


# Sol 2 - Bucket Sort
# O(n)
# n = len(nums)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for key in counter:
            buckets[counter[key]].append(key)

        res = []
        for i in range(len(nums), -1, -1):
            res += buckets[i]
            if len(res) >= k:
                return res[:k]
        return res[:k]