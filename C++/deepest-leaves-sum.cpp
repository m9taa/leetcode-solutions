#include <vector>


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
    int deepestLeavesSum(TreeNode* root) {
        // Time:  O(n)
        // Space: O(n)
        std::vector<TreeNode*> prev, current = {root};
        while (!current.empty()) {
            prev = std::move(current);
            for (const TreeNode* node: prev) {
                if (node) {
                    if (node->left) {
                        current.emplace_back(node->left);
                    }
                    if (node->right) {
                        current.emplace_back(node->right);
                    }
                }
            }
        }
        int result = 0;
        for (const TreeNode* node: prev) {
            result += node->val;
        }
        return result;
    }
};