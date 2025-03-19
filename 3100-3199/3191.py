from typing import List


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                count += 1
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1

        if nums[-3:] != [1, 1, 1]:
            count = -1

        return count


# nums = [0, 1, 1, 1, 0, 0]
nums = [0, 1, 1, 1]
print(Solution().minOperations(nums))
print(nums)
