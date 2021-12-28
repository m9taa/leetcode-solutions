from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time:  O(n)
        # Space: O(1)
        max_count = 2
        count = 1
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                if count < max_count:
                    slow += 1
                    nums[slow] = nums[fast]
                    count += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                count = 1
            fast += 1
        return slow + 1
