from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        low = 1
        high = max(candies)
        mid = (low + high) // 2
        while low <= high:
            children = 0
            for c in candies:
                children += c // mid

            if children >= k:
                low = mid + 1
                mid = (low + high) // 2
            else:
                high = mid - 1
                mid = (low + high) // 2

            print(low, high)

        return mid
        


# candies = [5, 8, 6]
# k = 3
candies = [2,5]
k = 11

print(Solution().maximumCandies(candies, k))
