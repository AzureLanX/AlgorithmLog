from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        re_prefix = [1] * n
        for i in range(n):
            if i == 0:
                prefix[i] = prefix[i] * nums[i]
                re_prefix[n-i-1] = re_prefix[n - i - 1] * nums[n - i -1]
            else:
                prefix[i] = nums[i] * prefix[i-1]
                re_prefix[n-i-1] = nums[n-i-1] * re_prefix[n-i]
        
        res = [0] * n
        for i in range(n):
            if i == 0:
                res[i] = re_prefix[i+1]
            elif i == n-1:
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i-1] * re_prefix[i+1]
        return res