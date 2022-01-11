from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> List[int]:
        # Time:  O(n)
        # Space: O(n)
        result = []
        if root:
            self._preorder(root, result)
        return result

    def _preorder(self, node: Node, result: List[int]) -> None:
        result.append(node.val)
        for child in node.children:
            self._preorder(child, result)


class Solution2:

    def preorder(self, root: Node) -> List[int]:
        # Time:  O(n)
        # Space: O(n)
        if not root:
            return []

        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(reversed(node.children))
        return result
