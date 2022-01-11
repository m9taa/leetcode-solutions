// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    int sumRootToLeaf(TreeNode* root) {
        // Time:  O(n)
        // Space: O(h)
        return sumNode(root, 0);
    }
private:
    int sumNode(TreeNode* node, int val) {
        if (!node) {
            return 0;
        }

        val = val * 2 + node->val;
        if (!node->left && !node->right) {
            return val;
        }

        return sumNode(node->left, val) + sumNode(node->right, val);
    }
};