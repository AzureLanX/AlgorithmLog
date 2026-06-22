from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        temp = 0
        for i in range(len(nums)):
            if temp == total - nums[i] - temp:
                return i
            temp += nums[i]
        return -1
        