from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + r >> 1
            # mid 比 l,r 都大,mid 取代min(l,r)成为新的边界
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l