from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n_count = 0
        p_count = 0

        for n in nums:
            if n < 0:
                n_count += 1
            elif n > 0:
                p_count += 1

        return max(n_count, p_count)