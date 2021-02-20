# O(n * log(n))
# n = len(restaurants)

from typing import List


class Solution:
    def filterRestaurants(
        self,
        restaurants: List[List[int]],
        veganFriendly: int,
        maxPrice: int,
        maxDistance: int,
    ) -> List[int]:
        filteredRestaurants = filter(
            lambda x: self.filterFunction(x, veganFriendly, maxPrice, maxDistance),
            restaurants,
        )
        sortedRestaurants = sorted(
            filteredRestaurants, key=lambda x: (x[1], x[0]), reverse=True
        )
        return [x[0] for x in sortedRestaurants]

    def filterFunction(self, restaurant, veganFriendly, maxPrice, maxDistance):
        if veganFriendly > 0 and restaurant[2] <= 0:
            return False
        if restaurant[3] > maxPrice:
            return False
        if restaurant[4] > maxDistance:
            return False
        return True
