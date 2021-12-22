from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time:  O(logn)
        # Space: O(1)
        if not nums:
            return -1
        start = 0
        end = len(nums)
        while (start + 1 < end):
            m = start + (end - start) // 2
            if target < nums[m]:
                end = m
            else:
                start = m
        return start if nums[start] == target else -1
