import itertools


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Time:  O(n)
        # Space: O(n)
        carry = 0
        result = []
        for a_char, b_char in itertools.zip_longest(reversed(a), reversed(b), fillvalue=0):
            carry, residue = divmod(int(a_char) + int(b_char) + carry, 2)
            result.append(str(residue))
        if carry:
            result.append(str(carry))
        return "".join(reversed(result))
