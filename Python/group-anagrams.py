from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time:  O(n)
        # Space: O(n)
        bag = {}
        for s in strs:
            key = ''.join(sorted(s))
            bag.setdefault(key, list())
            bag[key].append(s)
        return list(bag.values())
