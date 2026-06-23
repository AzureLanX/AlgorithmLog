from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for cur in intervals:
            if cur[1] < newInterval[0]:
                res.append(cur)
            elif cur[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = cur
            else:
                newInterval = [min(newInterval[0],cur[0]),max(newInterval[1],cur[1])]
        res.append(newInterval)
        return res


