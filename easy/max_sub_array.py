from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_value, value = nums[0], nums[0]
        for i in range(1, len(nums)):
            if value > 0:
                value += nums[i]
            else:
                value = nums[i]
            max_value = max(max_value, value)

        return max_value

    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)
