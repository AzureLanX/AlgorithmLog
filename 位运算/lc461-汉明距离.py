class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bit = x ^ y
        res = 0
        while bit:
            bit -= bit & (-bit)
            res += 1
        return res