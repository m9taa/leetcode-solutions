from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time:  O(n)
        # Space: O(n)
        m = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in m:
                return i, m[diff]
            m[val] = i
