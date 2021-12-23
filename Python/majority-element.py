from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Time:  O(n)
        # Space: O(1)
        element = None
        counter = 0
        for num in nums:
            if counter == 0:
                element = num
                counter += 1
            else:
                if num == element:
                    counter += 1
                else:
                    counter -= 1
        return element
