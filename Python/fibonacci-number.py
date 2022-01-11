class Solution:
    def fib(self, n: int) -> int:
        # Time:  O(n)
        # Space: O(1)
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current
        return prev
