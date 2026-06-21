from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if self.binarySearch(row, target):
                return True
        return False

    def binarySearch(self, data: List[int], target: int) -> bool:
        l = 0
        r = len(data) - 1
        while l < r:
            mid = l + r >> 1
            if data[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return data[l] == target