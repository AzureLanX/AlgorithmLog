from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        nums = [0 for _ in range(1010)]
        for trip in trips:
            nums[trip[1]] += trip[0]
            nums[trip[2]] -= trip[0]
        
        for i in range(0,len(nums)):
            nums[i] = nums[i] + nums[i-1]
            if nums[i] > capacity:
                return False
        
        return True