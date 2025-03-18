from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        max_length = 0
        bitmask = 0

        early_stop = max(nums).bit_length()

        for right in range(len(nums)):
            while (bitmask & nums[right]) != 0:
                bitmask ^= nums[left]
                left += 1

            bitmask |= nums[right]

            max_length = max(max_length, right - left + 1)

            if max_length == early_stop:
                break

        return max_length

nums = [1, 3, 8, 48, 10]
print(Solution().longestNiceSubarray(nums))
