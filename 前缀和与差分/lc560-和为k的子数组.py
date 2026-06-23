from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0 for _ in range(len(nums)+1)]
        for i in range(len(nums)):
            prefix[i+1] = nums[i] + prefix[i]
        res = 0
        hash = {}
        for i in prefix:
            target = i - k
            res += hash.get(target, 0)
            hash[i] = hash.get(i, 0) + 1
        return res


