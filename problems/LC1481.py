# O(n)
# n = len(arr)

import collections


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        buckets = [[] for _ in range(len(arr) + 1)]
        counter = {}
        for i in arr:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        removed = 0
        for i in counter:
            buckets[counter[i]].append(i)

        for b in range(1, len(buckets)):
            for i in range(len(buckets[b])):
                if b <= k:
                    removed += 1
                    k -= b
                else:
                    break

        print(buckets)

        return len(counter) - removed