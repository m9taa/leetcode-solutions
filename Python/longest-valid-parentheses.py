class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Time:  O(n)
        # Space: O(n)
        max_len = 0
        stack = [-1]
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len
