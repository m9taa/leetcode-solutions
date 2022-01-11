from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # Time:  O(n)
        # Space: O(h)
        return self.sum_node(root, 0)

    def sum_node(self, node, val):
        if not node:
            return 0

        val = 2 * val + node.val

        if not (node.left or node.right):
            return val

        return self.sum_node(node.left, val) + self.sum_node(node.right, val)
