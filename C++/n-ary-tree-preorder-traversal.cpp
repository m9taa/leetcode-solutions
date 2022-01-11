#include <vector>


// Definition for a Node.
class Node {
public:
    int val;
    std::vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, std::vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};


class Solution {
public:
    std::vector<int> preorder(Node* root) {
        // Time:  O(n)
        // Space: O(n)
        std::vector<int> result;
        if (root) {
            _preorder(root, result);
        }
        return result;
    }
private:
    void _preorder(Node* node, std::vector<int>& result) {
        result.push_back(node->val);
        for (auto child: node->children) {
            _preorder(child, result);
        }
    }
};