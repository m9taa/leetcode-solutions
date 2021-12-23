class Solution:
    def hammingWeight(self, n: int) -> int:
        # Time:  O(1)
        # Space: O(1)
        result = 0
        while (n != 0):
            result += n & 1
            n >>= 1
        return result
